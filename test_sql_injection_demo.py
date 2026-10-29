"""Testes de regressão locais; não acessam rede nem sistemas externos."""

import unittest

from examples.sql_injection.demo_login import (
    create_demo_database,
    login_parameterized,
    login_unsafe,
)


class SqlInjectionDemoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = create_demo_database()

    def tearDown(self) -> None:
        self.connection.close()

    def test_unsafe_query_accepts_injected_username_in_demo(self) -> None:
        result = login_unsafe(self.connection, "alice' -- ", "wrong-password")
        self.assertEqual(result, (1, "alice"))

    def test_parameterized_query_treats_input_as_data(self) -> None:
        result = login_parameterized(self.connection, "alice' -- ", "wrong-password")
        self.assertIsNone(result)

    def test_parameterized_query_accepts_demo_credentials(self) -> None:
        result = login_parameterized(self.connection, "alice", "demo-only-password")
        self.assertEqual(result, (1, "alice"))


if __name__ == "__main__":
    unittest.main()
