# vulnerability-analysis

Skill educacional do DIO Agent para conduzir uma análise defensiva de vulnerabilidades com contexto, evidências e avaliação de risco antes de recomendar uma correção.

## O que orienta

- Perguntar sobre ativo, ambiente, autorização e escopo antes de orientar testes ativos.
- Separar evidência, hipótese e informação ausente.
- Avaliar impacto na confidencialidade, integridade e disponibilidade.
- Estimar probabilidade e severidade por uma matriz didática documentada.
- Usar CWE/OWASP e MITRE ATT&CK somente quando o mapeamento fizer sentido.
- Propor correção da causa raiz e validação em laboratório ou staging autorizado.

O arquivo `SKILL.md` é o roteiro que o agente segue. Esta página explica a skill para pessoas; não contém respostas prontas para uma vulnerabilidade específica.

## Exemplo de uso

Peça ao agente para revisar um trecho de código e informar o que ainda precisa saber antes de concluir. Para sistemas expostos ou de produção, informe primeiro o escopo autorizado; a skill orienta o agente a perguntar antes de sugerir comandos.

## Referências

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
