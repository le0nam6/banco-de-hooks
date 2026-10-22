# Banco de Hooks Virais BR

Banco de hooks (ganchos) e técnicas de retenção para Reels, Shorts e TikTok que viralizam no **orgânico** no **Brasil**, feito para ser usado por um agente do Claude.

- **381 hooks** em **25 categorias**, cada um com template + exemplo pronto em português do Brasil
- **237 hooks com prova**: frases reais de reels brasileiros com views e envios
- **286 reels brasileiros minerados** (hook falado, views, envios, duração) em [`data/reels-minerados.csv`](data/reels-minerados.csv)
- Teoria dos melhores do mundo (Kallaway, Jenny Hoyos, Hormozi, Brendan Kane) + prática dos melhores do Brasil (Fernando Miranda, Thiago Nigro, Izabela Anholett, Marcelo Toledo…)
- 50 ideias de hook visual, conectores, re-hooks, finais e CTAs, 6 estruturas de roteiro, checklist de auditoria

## Mapa

| Arquivo | Conteúdo |
|---|---|
| [`PERSONAGEM.md`](PERSONAGEM.md) | Quem é o agente: o Dante, diretor criativo sênior, franco e provocador, que pergunta antes de decidir e abre caminhos em tema difícil |
| [`SKILL.md`](SKILL.md) | Instruções para o agente (pode ser instalado como skill do Claude) |
| [`01-fundamentos.md`](01-fundamentos.md) | Métricas do Instagram, dados da mineração, contraste A→B, 4 componentes, 6 peças, 4 erros |
| [`02-especialistas.md`](02-especialistas.md) | Mineração: quem ensina e quem executa (com padrões e números) |
| [`03-hooks-verbais.md`](03-hooks-verbais.md) | **O banco**: 306 hooks em tabelas por categoria (gerado do JSON) |
| [`04-hooks-visuais-e-texto.md`](04-hooks-visuais-e-texto.md) | Primeiro frame, texto na tela, 50 hooks visuais, áudio |
| [`05-retencao.md`](05-retencao.md) | Foreshadow, conectores, re-hooks, ritmo de edição, finais e CTAs |
| [`06-estruturas-de-roteiro.md`](06-estruturas-de-roteiro.md) | 6 estruturas completas com exemplo |
| [`07-checklist-e-auditoria.md`](07-checklist-e-auditoria.md) | Nota de 0 a 10, testes, diagnóstico pelos Insights, protocolo de teste |
| [`08-pautas-que-viralizam-no-brasil.md`](08-pautas-que-viralizam-no-brasil.md) | Temas, palavras e ingredientes que funcionam no Brasil |
| [`09-roteiro-humanizado-anti-ai-slop.md`](09-roteiro-humanizado-anti-ai-slop.md) | Lista negra de vícios de IA, padrões de estrutura, oralidade brasileira, antes e depois, prompt de revisão |
| [`10-familiaridade.md`](10-familiaridade.md) | Por que o hook precisa de algo que o público reconhece no 1º segundo (Cialdini, Hanah Franklin, MAYA) e um banco de âncoras do Brasil |
| [`11-caso-me-demiti.md`](11-caso-me-demiti.md) | Caso real: seis ganchos recusados, a condução por perguntas e o gancho aprovado, com as regras que saíram dele |
| [`12-outliers-outubro-2026.md`](12-outliers-outubro-2026.md) | O que os 82 outliers coletados pelo Claude in Chrome mostram, e a tabela detalhada em `data/hooks-detalhados.csv` |
| [`PROMPT-CLAUDE-IN-CHROME.md`](PROMPT-CLAUDE-IN-CHROME.md) | Prompt para minerar novos hooks ao vivo no seu navegador |
| [`data/hooks.json`](data/hooks.json) | Fonte de verdade dos hooks (para o agente filtrar) |
| [`data/reels-minerados.csv`](data/reels-minerados.csv) | Dataset dos reels reais |
| [`data/meus-testes.csv`](data/meus-testes.csv) | Planilha para registrar os resultados dos seus vídeos |
| [`scripts/hooks.py`](scripts/hooks.py) | Gera o `03` e permite sortear e buscar hooks |

## Como usar com o seu agente do Claude

**Opção 1: como skill (recomendado).** Copie a pasta para o diretório de skills:

```bash
cp -r banco-de-hooks ~/.claude/skills/hooks-virais-br    # skill pessoal
# ou, dentro de um projeto:
cp -r banco-de-hooks .claude/skills/hooks-virais-br
```

Depois peça: *“Me dá 3 hooks para um vídeo sobre como o Coco Bambu usa o aniversário como marketing.”*

**Opção 2: em um Projeto do Claude.ai.** Suba `SKILL.md` como instrução do projeto e os arquivos `01` a `08` + `data/hooks.json` como conhecimento.

**Opção 3: junto com a sua skill de roteiro.** Na sua skill de roteiro (ex.: `leonam-roteiro`), adicione: *“Para o hook, siga `banco-de-hooks/SKILL.md` e audite com `07-checklist-e-auditoria.md`.”*

## Consultar pelo terminal

```bash
python3 scripts/hooks.py listar                 # categorias
python3 scripts/hooks.py sortear --cat NQ --n 5 # 5 hooks de notícia quente
python3 scripts/hooks.py buscar "bilionário"    # busca
python3 scripts/hooks.py provados --n 30        # só os reais minerados
python3 scripts/hooks.py build                  # regera o 03 depois de editar o JSON
```

## Alimentar o banco (o que faz ele dar resultado no SEU perfil)

O banco é o ponto de partida. O que faz ele funcionar no seu perfil é o ciclo:

1. Gere 3 hooks por vídeo (categorias diferentes).
2. Teste 2 como **Trial Reels**.
3. Registre skip rate, retenção aos 3 s, views e envios em `data/meus-testes.csv`.
4. Hook vencedor (skip rate < 30% ou retenção aos 3 s > 60%) entra no `data/hooks.json` com a sua prova.
5. A cada mês, rode o prompt do Claude in Chrome para minerar outliers novos do seu nicho.

Com o tempo, o banco vira o mesmo que o Fernando Miranda tem: uma IA treinada nos **seus** vídeos mais virais.

## Metodologia e limites

- Reels minerados em outubro de 2026 a partir de perfis públicos (índice Oriane, via Firecrawl). Views e envios mudam com o tempo.
- O método de Fernando Miranda foi extraído da transcrição completa do vídeo dele com Dener Lippert sobre o método da Staage.
- A teoria internacional foi traduzida e adaptada, não copiada.
- Os hooks sem prova são modelos escritos a partir dos padrões. Fatos citados nos exemplos de modelo são ilustrativos: confirme antes de gravar.
- Os hooks reais servem de **estrutura**. Não copie o roteiro de outro criador palavra por palavra.
