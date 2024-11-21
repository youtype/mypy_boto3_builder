"""
Backport of `boto3.resources.model`.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore import xform_name
from botocore.model import Shape, StructureShape


class Identifier:
    """
    A resource identifier, given by its name.
    """

    def __init__(self, name: str, member_name: str | None = None) -> None:
        self.name = name
        self.member_name = member_name


class Action:
    """
    A service operation action.
    """

    def __init__(
        self,
        name: str,
        definition: dict[str, Any],
        resource_defs: dict[str, Any],
    ) -> None:
        self._definition = definition

        self.name = name
        self.request: Request | None = None
        if "request" in definition:
            self.request = Request(definition.get("request", {}))
        self.resource: ResponseResource | None = None
        if "resource" in definition:
            self.resource = ResponseResource(definition.get("resource", {}), resource_defs)
        self.path: str | None = definition.get("path")


class DefinitionWithParams:
    """
    An item which has parameters exposed via the ``params`` property.
    """

    def __init__(self, definition: dict[str, Any]) -> None:
        self._definition = definition

    @property
    def params(self) -> "list[Parameter]":
        """
        Get a list of auto-filled parameters for this request.
        """
        params: list[Parameter] = []

        params.extend(Parameter(**item) for item in self._definition.get("params", []))

        return params


class Parameter:
    """
    An auto-filled parameter which has a source and target.
    """

    def __init__(
        self,
        target: str,
        source: str,
        name: str | None = None,
        path: str | None = None,
        value: str | float | bool | None = None,  # noqa: FBT001
        **kwargs: str,
    ) -> None:
        self.target = target
        self.source = source
        self.name = name
        self.path = path
        self.value = value


class Request(DefinitionWithParams):
    """
    A service operation action request.
    """

    def __init__(self, definition: dict[str, Any]) -> None:
        super().__init__(definition)
        self.operation: str = definition.get("operation") or ""


class Waiter(DefinitionWithParams):
    """
    An event waiter specification.
    """

    PREFIX = "WaitUntil"

    def __init__(self, name: str, definition: dict[str, Any]) -> None:
        super().__init__(definition)
        self.name = name
        self.waiter_name: str | None = definition.get("waiterName")


class ResponseResource:
    """
    A resource response to create after performing an action.
    """

    def __init__(
        self, definition: dict[str, Any], resource_defs: dict[str, dict[str, Any]]
    ) -> None:
        self._definition = definition
        self._resource_defs = resource_defs
        self.type: str = definition.get("type") or ""
        self.path: str | None = definition.get("path")

    @property
    def identifiers(self) -> list[Parameter]:
        """
        A list of resource identifiers.
        """
        identifiers: list[Parameter] = []

        identifiers.extend(Parameter(**item) for item in self._definition.get("identifiers", []))

        return identifiers

    @property
    def model(self) -> "ResourceModel":
        """
        Get the resource model for the response resource.
        """
        return ResourceModel(self.type, self._resource_defs[self.type], self._resource_defs)


class Collection(Action):
    """
    A group of resources. See :py:class:`Action`.
    """

    @property
    def batch_actions(self) -> list[Action]:
        """
        Get a list of batch actions supported by the resource type.
        """
        if not self.resource:
            return []
        return self.resource.model.batch_actions


class ResourceModel:
    """
    A model representing a resource, defined via a JSON description.
    """

    def __init__(
        self, name: str, definition: dict[str, Any], resource_defs: dict[str, Any]
    ) -> None:
        self._definition = definition
        self._resource_defs = resource_defs
        self._renamed: dict[tuple[str, str], str] = {}

        self.name = name
        self.shape: str | None = definition.get("shape")

    def _get_name(self, category: str, name: str, snake_case: bool = True) -> str:  # noqa: FBT001, FBT002
        """
        Get a possibly renamed value given a category and name.
        """
        if snake_case:
            name = xform_name(name)

        return self._renamed.get((category, name), name)

    def get_attributes(self, shape: Shape) -> dict[str, tuple[str, Shape]]:
        """
        Get a dictionary of attribute names to original name and shape.
        """
        attributes: dict[str, tuple[str, Shape]] = {}
        identifier_names = [i.name for i in self.identifiers]
        if not isinstance(shape, StructureShape):
            return attributes
        for name, member in shape.members.items():
            snake_cased = xform_name(name)
            if snake_cased in identifier_names:
                # Skip identifiers, these are set through other means
                continue
            snake_cased = self._get_name("attribute", snake_cased, snake_case=False)
            attributes[snake_cased] = (name, member)

        return attributes

    @property
    def identifiers(self) -> list[Identifier]:
        """
        Get a list of resource identifiers.
        """
        identifiers: list[Identifier] = []

        for item in self._definition.get("identifiers", []):
            name = self._get_name("identifier", item["name"])
            member_name = item.get("memberName", None)
            if member_name:
                member_name = self._get_name("attribute", member_name)
            identifiers.append(Identifier(name, member_name))

        return identifiers

    @property
    def load(self) -> Action | None:
        """
        Get the load action for this resource, if it is defined.
        """
        definition = self._definition.get("load")

        if definition is None:
            return None

        return Action("load", definition, self._resource_defs)

    @property
    def actions(self) -> list[Action]:
        """
        Get a list of actions for this resource.
        """
        actions: list[Action] = []

        for name, item in self._definition.get("actions", {}).items():
            action_name = self._get_name("action", name)
            actions.append(Action(action_name, item, self._resource_defs))

        return actions

    @property
    def batch_actions(self) -> list[Action]:
        """
        Get a list of batch actions for this resource.
        """
        actions: list[Action] = []

        for name, item in self._definition.get("batchActions", {}).items():
            action_name = self._get_name("batch_action", name)
            actions.append(Action(action_name, item, self._resource_defs))

        return actions

    def _get_has_definition(self) -> dict[str, dict[str, Any]]:
        """
        Get a ``has`` relationship definition from a model.
        """
        if self.name not in self._resource_defs:
            # This is the service resource, so let us expose all of
            # the defined resources as subresources.
            definition: dict[str, dict[str, Any]] = {}

            for name, resource_def in self._resource_defs.items():
                # It's possible for the service to have renamed a
                # resource or to have defined multiple names that
                # point to the same resource type, so we need to
                # take that into account.
                found = False
                has_items = self._definition.get("has", {}).items()
                for has_name, has_def in has_items:
                    if has_def.get("resource", {}).get("type") == name:
                        definition[has_name] = has_def
                        found = True

                if not found:
                    fake_has: dict[str, dict[str, Any]] = {
                        "resource": {"type": name, "identifiers": []}
                    }

                    for identifier in resource_def.get("identifiers", []):
                        fake_has["resource"]["identifiers"].append(
                            {"target": identifier["name"], "source": "input"}
                        )

                    definition[name] = fake_has
        else:
            definition = self._definition.get("has", {})

        return definition

    def _get_related_resources(self, subresources: bool) -> list[Action]:  # noqa: FBT001
        """
        Get a list of sub-resources or references.
        """
        resources: list[Action] = []

        for name, definition in self._get_has_definition().items():
            if subresources:
                action_name = self._get_name("subresource", name, snake_case=False)
            else:
                action_name = self._get_name("reference", name)
            action = Action(action_name, definition, self._resource_defs)
            if not action.resource:
                continue

            data_required = False
            for identifier in action.resource.identifiers:
                if identifier.source == "data":
                    data_required = True
                    break

            if (subresources and not data_required) or (not subresources and data_required):
                resources.append(action)

        return resources

    @property
    def subresources(self) -> list[Action]:
        """
        Get a list of sub-resources.
        """
        return self._get_related_resources(subresources=True)

    @property
    def references(self) -> list[Action]:
        """
        Get a list of reference resources.
        """
        return self._get_related_resources(subresources=False)

    @property
    def collections(self) -> list[Collection]:
        """
        Get a list of collections for this resource.
        """
        collections: list[Collection] = []

        for name, item in self._definition.get("hasMany", {}).items():
            collection_name = self._get_name("collection", name)
            collections.append(Collection(collection_name, item, self._resource_defs))

        return collections

    @property
    def waiters(self) -> list[Waiter]:
        """
        Get a list of waiters for this resource.
        """
        waiters: list[Waiter] = []

        for name, item in self._definition.get("waiters", {}).items():
            waiter_name = self._get_name("waiter", Waiter.PREFIX + name)
            waiters.append(Waiter(waiter_name, item))

        return waiters
