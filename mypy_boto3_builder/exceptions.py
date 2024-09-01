"""
Exceptions for mypy_boto3_builder.
"""


class BuilderError(ValueError):
    """
    Base error for mypy_boto3_builder.
    """


class JinjaManagerError(BuilderError):
    """
    Base JinjaManager exception.
    """


class ShapeParserError(BuilderError):
    """
    Main error for ShapeParser.
    """


class BuildError(BuilderError):
    """
    Error during build process.
    """


class BuildEnvError(BuildError):
    """
    Error during getting 3rd party data.
    """


class BuildInternalError(BuildError):
    """
    Error on invalid build.
    """


class TypeAnnotationError(BuildInternalError):
    """
    Error on invalid internal type annotation.
    """


class StructureError(BuildInternalError):
    """
    Error on invalid internal structure.
    """
