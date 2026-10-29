# Demonstração local de SQL Injection

Este exercício usa um banco SQLite **em memória**, uma conta fictícia e um programa de terminal. Não inicia servidor e não acessa rede.

Na raiz do repositório, execute a versão vulnerável:

```bash
python -m examples.sql_injection.demo_login --mode unsafe
```

Para reproduzir o problema somente nesse laboratório, informe o usuário `alice' -- ` e qualquer senha. A concatenação altera a estrutura da consulta e a demonstração pode aceitar o acesso sem a senha correta.

Compare com a versão corrigida:

```bash
python -m examples.sql_injection.demo_login --mode fixed
```

Use a mesma entrada: a consulta parametrizada trata o texto como valor literal e não deve conceder acesso. O exemplo mantém senha fictícia em texto puro apenas para isolar SQL Injection; sistemas reais precisam armazenar senhas com algoritmo apropriado de hashing e implementar controles adicionais.

## Validação automatizada

Na raiz do projeto:

```bash
python -m unittest discover -s tests -v
```

Os testes usam somente SQLite em memória. Eles confirmam o comportamento vulnerável no exercício e a regressão esperada na função parametrizada; não são um scanner nem uma recomendação para testar serviços de terceiros.

## Mapeamento e correção

A classe da falha é SQL Injection (CWE-89). Se uma aplicação pública for explorada para obter acesso inicial, MITRE ATT&CK T1190 pode ser pertinente; não é um mapeamento automático para qualquer SQL Injection. A mitigação principal é separar a consulta dos valores com parâmetros. Veja [CWE-89](https://cwe.mitre.org/data/definitions/89.html), [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) e `agent/knowledge/security-basics.md`.
