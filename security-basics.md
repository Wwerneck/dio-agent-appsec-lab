# Fundamentos de segurança da informação

Este arquivo apoia explicações educacionais e análises defensivas. Use-o junto com a skill `vulnerability-analysis`; ele não substitui uma avaliação técnica completa.

## Conceitos essenciais

- **Vulnerabilidade:** fraqueza em software, configuração, processo ou controle que pode ser explorada ou causar falha.
- **Ameaça:** agente, evento ou condição capaz de causar dano aproveitando uma vulnerabilidade.
- **Risco:** combinação entre a chance de um cenário ocorrer e o impacto esperado. O risco depende do ativo, exposição, controles e contexto de negócio.
- **Exploração:** uso de uma vulnerabilidade para produzir um efeito. A existência de uma falha não prova que ela foi explorada.

## Tríade CIA

- **Confidencialidade:** impedir acesso ou divulgação não autorizada. Exemplo de impacto: exposição de dados pessoais ou segredos.
- **Integridade:** preservar exatidão e completude. Exemplo: alteração não autorizada de registros ou transações.
- **Disponibilidade:** manter sistemas e dados acessíveis quando necessários. Exemplo: interrupção de serviço ou perda de acesso.

Uma falha pode afetar mais de uma dimensão. Registre quais são afetadas e por qual evidência.

## Estimativa didática de severidade

Use escalas de 1 a 5 para impacto e probabilidade estimada. Calcule `impacto × probabilidade` e classifique:

| Nota | Impacto (CIA) | Probabilidade estimada |
|---:|---|---|
| 1 | Mínimo, sem efeito relevante nos dados ou serviço | Improvável; ambiente isolado e pré-condições ausentes |
| 2 | Limitado e facilmente reversível | Baixa; acesso restrito e várias pré-condições necessárias |
| 3 | Relevante em parte do ativo ou para poucos usuários | Possível; caminho plausível, controles parcialmente eficazes ou contexto incompleto |
| 4 | Grave para dados, funções importantes ou continuidade | Alta; alcançável no contexto descrito, poucas barreiras eficazes |
| 5 | Muito grave, amplo ou difícil de reverter | Muito alta; exploração observada ou condições simples e confirmadas no escopo |

Não atribua nota 4–5 só porque uma falha é conhecida. Baseie a nota no ativo e nas condições verificadas; indique lacunas.

| Pontuação | Severidade didática |
|---:|---|
| 1–4 | Baixa |
| 5–9 | Moderada |
| 10–16 | Alta |
| 17–25 | Crítica |

Explique os motivos dos valores; não apresente a estimativa como estatística medida. Esta matriz é uma ferramenta didática, não o CVSS nem uma substituição para política corporativa. Quando faltarem dados, registre a incerteza e peça contexto antes de fechar a classificação.

## SQL Injection

SQL Injection ocorre quando dados não confiáveis são incorporados à sintaxe de uma consulta. A defesa primária é separar estrutura da consulta e valores por meio de consultas parametrizadas ou prepared statements. Validação por allowlist e privilégio mínimo são camadas complementares, não substitutos da parametrização.

O exemplo deste repositório usa somente SQLite em memória, registros fictícios e um processo local de terminal. Não conecte o exemplo a dados ou serviços reais.

### MITRE ATT&CK

MITRE ATT&CK descreve comportamentos adversários, não classes de falha de software. **T1190 — Exploit Public-Facing Application** pode ser pertinente quando um adversário explora uma aplicação exposta à internet para obter acesso inicial. Isso não significa que todo SQL Injection seja automaticamente T1190. Explique a condição e não invente mapeamento quando os fatos não sustentarem a associação.

## Boas práticas de defesa

- Use consultas parametrizadas para valores enviados pelo usuário.
- Aplique menor privilégio a contas de aplicação e banco de dados.
- Mantenha dependências e plataformas atualizadas e revise configurações expostas.
- Evite revelar mensagens internas, consultas ou rastros de pilha a usuários.
- Registre eventos relevantes sem gravar senhas, tokens ou dados desnecessários.
- Teste correções em testes automatizados e ambiente de laboratório ou staging.
- Tenha inventário de ativos, backups testados, gestão de segredos e plano de resposta.
- Faça testes em sistemas de terceiros somente com autorização explícita e escopo definido.

## Fontes de referência

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
