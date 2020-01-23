import unittest

from mypy_boto3_builder.structures.paginator import Paginator


class PaginatorTestCase(unittest.TestCase):
    def test_init(self) -> None:
        paginator = Paginator(name="name", operation_name="my_operation_name")
        self.assertEqual(paginator.name, "name")
        self.assertEqual(paginator.operation_name, "my_operation_name")

    def test_get_client_method(self) -> None:
        paginator = Paginator(name="name", operation_name="my_operation_name")
        result = paginator.get_client_method()
        self.assertEqual(result.name, "get_paginator")
        self.assertEqual(result.return_type.name, "name")
        self.assertEqual(result.arguments[1].type.children[0], "my_operation_name")
