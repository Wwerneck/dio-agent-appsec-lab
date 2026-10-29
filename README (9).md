# 🤖 DIO Agent — Especialização Educacional em AppSec

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

Este repositório é uma extensão educacional do projeto [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent), baseada no commit `3751c04fac4813482a3c54a067482759215a69cf`. A melhoria adiciona uma especialização defensiva em AppSec: o agente busca contexto e autorização, separa evidências de hipóteses, estima impacto e probabilidade e propõe correções verificáveis.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.

- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |

Ele conhece os formatos da DIO: Bootcamps, Formações, Acelerações, Cursos, English4Tech, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, que tem limites de uso mais generosos para quem está começando. Mas qualquer harness moderno funciona.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

Escolha um e siga o passo a passo da documentação oficial dele. Cada documentação já traz tudo certinho para o seu sistema, então a instalação é tranquila.

### 2️⃣ Configure o DIO Agent

Agora você vai baixar este repositório para o seu computador. Escolha a forma mais simples para você:

**Opção A: com Git** (se você já usa Git)

```bash
git clone https://github.com/Wwerneck/dio-agent-appsec-lab.git
```

**Opção B: baixando o .zip** (se você não usa Git)

Na página do repositório no GitHub, clique no botão verde **Code** e depois em **Download ZIP**. Em seguida, extraia a pasta em um lugar fácil de encontrar.

Com o repositório baixado, abra a pasta `dio-agent-appsec-lab` no harness que você instalou. Cada harness tem o seu jeito de abrir uma pasta de projeto, e a documentação dele mostra como fazer isso. Para o Hermes, abra um terminal **na raiz dessa pasta** e inicie `hermes`, conforme a [documentação oficial](https://hermes-agent.nousresearch.com/docs).

E é só isso! O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

> 🔄 **Fique de olho nas atualizações.** Não importa se você usou o Git ou o .zip: o repositório do DIO Agent evolui com o tempo. De tempos em tempos, vale voltar aqui e pegar a versão mais recente. Quem usou Git pode rodar `git pull` (ou pedir pro próprio DIO Agent rodar); quem baixou o .zip pode baixar de novo. Assim o seu mentor está sempre com o melhor que a gente tem a oferecer.

### 3️⃣ Hands On!

Agora é só conversar. Você pode falar naturalmente, com as suas palavras. Mas, principalmente nas primeiras vezes, vale usar um modelo de prompt pronto: é só copiar e preencher os campos entre colchetes. Quanto mais contexto você dá, melhor o agente ajuda.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos (se possível, com materiais complementares).
- Meu objetivo: [ex: aprender mais sobre IA, ser dev back-end, concluir um bootcamp]
- Experiência ou carreira da DIO: [URL ou nome do bootcamp/formação, ou de uma carreira da DIO]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou descreva]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código atual: [cole aqui, se for Desafio de Código]
- Link do repositório base: [cole aqui, se for Desafio de Projeto]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
- Onde apareceu: [ex: no curso X de um bootcamp] (opcional)
```

Não precisa de comando especial nem de formato perfeito: o agente conduz a conversa a partir daí e pede mais detalhes se precisar.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. O repositório organiza cada habilidade em um guia próprio:

| Skill | Para que serve |
|-------|----------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Ajuda a revisar a apresentação de projetos |
| [Pesquisa na web](skills/web-search/SKILL.md) | Fundamenta respostas com informações atuais e fontes |
| [Análise de vulnerabilidade](skills/vulnerability-analysis/SKILL.md) | Orienta análise defensiva, avaliação de risco e correção |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

Esta extensão inclui também `vulnerability-analysis`, indicada quando a pessoa pede revisão de segurança, priorização de risco, correção ou validação de uma mitigação.

---

## 🛡️ Extensão educacional de AppSec

### Especialização e melhoria escolhida

O agente orienta análise defensiva de vulnerabilidades. A melhoria é um formato estável de avaliação: impacto na confidencialidade, integridade e disponibilidade (CIA), probabilidade estimada, severidade didática, confiança, incertezas, correção prioritária e validação segura. Para sistema exposto ou produção, a skill pede contexto e autorização antes de sugerir testes ativos ou comandos.

A matriz de risco é didática (impacto de 1–5 × probabilidade estimada de 1–5) e não deve ser confundida com CVSS. O mapeamento MITRE ATT&CK é condicional: T1190 só é citado quando a exploração de uma aplicação pública para acesso inicial corresponde ao cenário descrito.

### Arquivos criados e alterados

| Arquivo | Alteração |
|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Processo passo a passo, limites, avaliação de risco e formato de resposta |
| `skills/vulnerability-analysis/README.md` | Explicação da skill para pessoas |
| `agent/knowledge/security-basics.md` | Vulnerabilidade, ameaça, risco, CIA, práticas defensivas e referências |
| `agent/persona.md` | Orientação para priorizar escopo, autorização e correção defensiva |
| `AGENTS.md` | Inclusão da base de conhecimento, gatilho da skill e regra de contexto em segurança |
| `skills/README.md` | Inclusão da nova skill no catálogo |
| `examples/sql_injection/` | Demonstração local vulnerável e função parametrizada corrigida |
| `tests/test_sql_injection_demo.py` | Testes locais de regressão com SQLite em memória |
| `docs/evidence/README.md` | Roteiro para capturas reais do agente no Hermes, sem imagens fabricadas |

### Executar a demonstração local

Use Python 3.10 ou superior. Não há dependências externas para o exemplo, que cria um banco SQLite volátil.

```bash
# Na raiz do repositório, demonstração vulnerável
python -m examples.sql_injection.demo_login --mode unsafe

# Repetir no código corrigido
python -m examples.sql_injection.demo_login --mode fixed

# Validar as duas versões com testes locais
python -m unittest discover -s tests -v
```

Na versão vulnerável, o exemplo usa somente a conta fictícia `alice`. A entrada `alice' -- ` demonstra como a concatenação pode alterar a consulta neste banco em memória. Na versão corrigida, a mesma entrada é tratada como valor literal por meio de parâmetros. Não use o exemplo com credenciais, dados ou serviços reais. A senha em texto puro serve apenas para isolar a falha didática; não é um padrão de armazenamento seguro.

### Usar a skill no Hermes

1. Instale o Hermes seguindo a documentação oficial listada no README.
2. Abra o terminal com o diretório atual na raiz deste repositório.
3. Inicie `hermes`; o harness carrega o `AGENTS.md` e os arquivos da skill.
4. Peça uma análise do código em `examples/sql_injection/demo_login.py` e informe que é um laboratório local autorizado.
5. Depois, peça revisão da função `login_parameterized` e compare a avaliação antes/depois.

Para avaliar as perguntas de contexto, descreva um cenário de servidor exposto sem presumir autorização e observe se o agente pergunta sobre ativo, escopo e permissão antes de sugerir testes. Não execute nenhuma ação contra sistemas externos.

### Evidências

O roteiro em [`docs/evidence/README.md`](docs/evidence/README.md) lista capturas úteis da conversa real no Hermes. As imagens não foram fabricadas; adicione suas próprias capturas após executar o harness, removendo segredos e dados pessoais.

### Fontes de segurança

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [MITRE ATT&CK T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                        Este guia
├── AGENTS.md                        Definição do agente (lida por qualquer harness)
├── CLAUDE.md                        Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                   Personalidade, tom e postura AppSec
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       ├── learning-experiences.md  Os formatos de aprendizado da DIO
│       └── security-basics.md       Risco, CIA e práticas de defesa
│
├── skills/
│   ├── README.md                    O que são skills
│   ├── study-plan/                  Skill: plano de estudos
│   ├── unblock-challenge/           Skill: destravar desafio
│   ├── explain-concept/             Skill: explicar conceito
│   └── vulnerability-analysis/      Skill: análise defensiva de vulnerabilidade
│
├── examples/sql_injection/          Exemplo local vulnerável e corrigido
├── tests/                           Testes de regressão locais
└── docs/
    ├── glossary.md                  Glossário de termos
    ├── security-review-scenarios.md Roteiro de avaliação da skill
    └── evidence/                    Orientação para capturas reais
```

> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele, então você pode usar o harness que preferir.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill* e *prompt* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
