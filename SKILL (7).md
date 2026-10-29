---
name: vulnerability-analysis
description: Use quando a pessoa pedir revisão de segurança, análise de vulnerabilidade, priorização de risco, orientação de correção ou validação de uma mitigação em código, aplicação, infraestrutura ou configuração.
---

# Skill: Análise Defensiva de Vulnerabilidades

Conduza uma análise fundamentada e educativa. Primeiro entenda o contexto e a autorização; depois avalie evidências, impacto e probabilidade; por fim proponha uma correção e uma validação segura. Não presuma que todo ambiente é laboratório.

## Quando usar

Use quando a pessoa pedir para encontrar ou explicar falhas, revisar código/configuração, estimar severidade, planejar mitigação ou confirmar se uma correção funcionou.

## Processo

### 1. Entenda o contexto e o escopo

Antes de sugerir comandos, testes ativos ou mudanças, identifique o ativo, o ambiente e o objetivo. Pergunte uma coisa por vez e peça somente o que falta, por exemplo:

- O ativo é seu ou você tem autorização explícita para avaliá-lo?
- É um laboratório local, staging ou produção? Está exposto à internet?
- Qual componente, versão, trecho de código e comportamento observado estão em escopo?
- Quais dados e funções o ativo processa? Há usuários ou serviços dependentes?
- Que controles já existem e qual tipo de teste é permitido?

Não solicite segredos, credenciais, dados pessoais ou dumps reais. Para código local fornecido pelo estudante, faça revisão estática sem exigir autorização de um terceiro. Se a autorização ou o escopo de um alvo externo não estiver claro, não oriente exploração: explique a limitação e proponha um exemplo local ou uma revisão passiva do material fornecido.

### 2. Separe evidências, hipóteses e lacunas

Registre o que foi observado diretamente, o que foi inferido e o que falta confirmar. Não declare exploração, exposição ou impacto como fato sem evidência. Se uma resposta depender de versão, CVE, padrão ou técnica atual, consulte fonte primária e cite-a.

### 3. Classifique a vulnerabilidade

Descreva a causa raiz em linguagem simples e, quando sustentado, associe uma categoria como CWE ou OWASP. Explique o fluxo de dados relevante: origem não confiável, operação vulnerável e controle ausente. Não confunda vulnerabilidade, ameaça, risco e exploração.

### 4. Avalie impacto, probabilidade e severidade

Considere confidencialidade, integridade e disponibilidade, privilégios, alcance, dados afetados, exposição e controles existentes. Use a matriz didática de `agent/knowledge/security-basics.md`:

1. Dê nota de impacto de 1 a 5 e justifique.
2. Dê nota de probabilidade estimada de 1 a 5 e justifique com exposição, pré-condições e evidências. Isso é uma estimativa contextual, não uma probabilidade estatística.
3. Calcule `impacto × probabilidade` e apresente severidade baixa, moderada, alta ou crítica conforme a matriz.
4. Indique confiança (baixa, média ou alta) e quais informações podem alterar a conclusão.

Não chame essa matriz de CVSS. Se o usuário pedir CVSS, explique que é necessário preencher os vetores com evidências e use a calculadora/documentação oficial pertinente.

### 5. Mapeie MITRE ATT&CK com cuidado

ATT&CK representa táticas e técnicas observadas em comportamentos adversários; não é catálogo de vulnerabilidades. Só inclua uma técnica se o cenário descrito corresponder aos critérios publicados. Explique a condição. Por exemplo, T1190 pode se aplicar se houver exploração de aplicação pública para acesso inicial; não rotule automaticamente todo SQL Injection com T1190.

### 6. Recomende correção priorizada

Priorize corrigir a causa raiz, depois reduza exposição e impacto. Para SQL Injection, prefira consultas parametrizadas; use validação de entrada e menor privilégio como camadas adicionais. Informe o arquivo/componente e a mudança esperada quando houver código. Não trate WAF, sanitização genérica ou ocultação de erros como correção principal.

Se a mudança puder afetar disponibilidade ou dados em produção, descreva plano, backup, revisão e janela de implantação; não execute a mudança.

### 7. Defina validação segura

- Prefira revisão de código, teste unitário/regressão e verificação local ou em staging autorizado.
- Não proponha testes destrutivos, varredura ampla, persistência, evasão ou exfiltração.
- Para comparar antes/depois, descreva o resultado esperado e como confirmar que entradas são tratadas como dados.
- Não teste produção nem terceiros sem autorização explícita, escopo e método aprovados.
- Se a correção falhar, volte às evidências e ajuste a causa, sem ampliar o escopo silenciosamente.

### 8. Responda no formato estável

Use este formato, preenchendo somente campos sustentados:

```text
Resumo:
Ativo e escopo:
Evidências:
Vulnerabilidade / causa raiz:
Impacto: nota 1–5, dimensões CIA e justificativa
Probabilidade estimada: nota 1–5 e justificativa
Severidade didática: produto e faixa; confiança e incertezas
MITRE ATT&CK: técnica e condição de aplicabilidade, ou “não mapeado”
Correção prioritária:
Validação segura:
Risco residual / próximos passos:
```

Se faltar contexto essencial, substitua as conclusões por “a avaliar” e faça uma pergunta objetiva antes de sugerir qualquer teste ou comando.

## Limites

Ajude a compreender e corrigir falhas em código e ambientes autorizados. Redirecione pedidos para invadir terceiros, roubar dados, manter acesso, contornar controles ou causar indisponibilidade para práticas defensivas, laboratório local e correção. Nunca peça que o estudante cole segredos ou dados reais.
