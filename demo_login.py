"""Exemplo didático de SQL Injection em SQLite exclusivamente em memória.

Não inicia servidor, não conecta à rede e não usa contas ou dados reais.
"""

from __future__ import annotations

import argparse
import sqlite3


def create_demo_database() -> sqlite3.Connection:
    """Cria dados fictícios em banco volátil para a demonstração local."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    connection.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ("alice", "demo-only-password"),
    )
    connection.commit()
    return connection


def login_unsafe(
    connection: sqlite3.Connection, username: str, password: str
) -> tuple[int, str] | None:
    """Implementação intencionalmente vulnerável, apenas para análise local."""
    query = (
        "SELECT id, username FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    return connection.execute(query).fetchone()


def login_parameterized(
    connection: sqlite3.Connection, username: str, password: str
) -> tuple[int, str] | None:
    """Versão corrigida: os valores são vinculados como dados, não como SQL."""
    return connection.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("unsafe", "fixed"),
        required=True,
        help="Escolha a versão intencionalmente vulnerável ou a corrigida.",
    )
    args = parser.parse_args()

    print("Demonstração local: banco SQLite em memória e conta fictícia 'alice'.")
    print("Não use senhas ou dados reais.")
    username = input("Usuário de teste: ")
    password = input("Senha de teste: ")
    connection = create_demo_database()
    try:
        login = login_unsafe if args.mode == "unsafe" else login_parameterized
        result = login(connection, username, password)
        print("Acesso de demonstração concedido." if result else "Credenciais de demonstração inválidas.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
