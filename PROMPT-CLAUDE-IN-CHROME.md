# Prompt para o Claude in Chrome: mineração de hooks ao vivo

Use no Claude in Chrome com o Instagram aberto e logado no seu navegador. O resultado sai num formato que pode ser colado direto no `data/reels-minerados.csv` ou no `data/hooks.json` deste repositório.

**Como usar**
1. Abra `instagram.com` logado.
2. Abra o painel do Claude in Chrome e cole o prompt abaixo.
3. Troque o `[NICHO]` e, se quiser, a lista de perfis.
4. Vá acompanhando: ele abre perfil por perfil e para a cada 5 reels para você validar.

---

```text
Você vai minerar hooks (ganchos) de Reels que viralizaram no Instagram brasileiro, navegando comigo no meu navegador. O objetivo é alimentar um banco de hooks para o meu agente de roteiro. Meu nicho é [NICHO, ex.: marketing, IA e negócios].

PERFIS (nesta ordem; pode sugerir outros brasileiros do meu nicho que performem bem):
@fernandomiranda777, @thiago.nigro, @izabela.anholett, @marcelotoledo, @rafaelkiso, @denerlippert, @joeljota, @caiocarneiro, @nathfinancas, @rony, @guilhermebenchimol, @jhon_freitas, @paulo.ia

PARA CADA PERFIL:
1. Abra o perfil e vá na aba Reels.
2. Role até ver pelo menos 30 reels e anote o número de visualizações que aparece em cada miniatura.
3. Calcule a mediana de views do perfil. Selecione os 5 reels com MAIS views que estejam acima de 3x a mediana (são os “outliers”: o hook fez diferença, não só o tamanho do perfil). Ignore publi e collab com marca, a não ser que seja muito acima da média.
4. Abra cada reel selecionado e registre:
   - url
   - criador
   - views (da miniatura), curtidas e comentários (se visíveis)
   - duracao_s (aproximada)
   - texto_tela: o texto que aparece escrito no PRIMEIRO frame (se houver)
   - primeiro_frame: descreva em 1 linha o que aparece visualmente no primeiro segundo (rosto, produto, logo, lugar, print, movimento)
   - hook_falado: transcreva EXATAMENTE as 1 ou 2 primeiras frases faladas (ative as legendas automáticas se precisar; se não der para ouvir, use a legenda gerada ou escreva “[sem áudio legível]”)
   - confirmacao: a frase que vem logo depois do hook
   - foreshadow: se houver promessa do que vem no final, transcreva
   - final_cta: a última frase / o CTA do vídeo
   - legenda_1a_linha: a primeira linha da legenda do post
   - categoria: escolha UMA destas siglas → VE (verdade escondida), RV (revelação de status), IN (investigador), NQ (notícia quente), FU (futuro), CT (contrário), EX (experimento), PR (professor/lista), AL (erro/alerta), SU (confirma suspeita), HP (história pessoal), OR (origem improvável), NU (número chocante), BR (Brasil x mundo/regional), ID (identificação), PG (pergunta), AF (aforismo curto), MI (mito), BS (bastidores), IA (nicho IA), MK (nicho marketing), PV (prova visual), DB (debate), HU (humor), HZ (formato Hormozi)
   - template: reescreva o hook trocando o específico por [colchetes] (ex.: “[Famoso] agora é bilionário.”)
   - por_que_funciona: 1 frase com o contraste A → B
5. A cada 5 reels, PARE e me mostre a tabela parcial. Espere eu dizer “segue” antes de continuar.

REGRAS:
- Não invente nada. Se não conseguir ver um número ou ouvir uma frase, escreva “?”.
- Não curta, não comente, não siga e não envie mensagem em nenhum perfil. Só leitura.
- Não faça login, não mude configurações e não clique em anúncios ou links externos.
- Se o Instagram pedir verificação ou bloquear a rolagem, pare e me avise.
- Transcreva em português exatamente como foi falado (inclusive “tá”, “pra”, “galera”).

SAÍDA FINAL, em dois blocos:

BLOCO 1 · CSV (cabeçalho exatamente assim, separado por vírgula, campos de texto entre aspas):
criador,views,envios,curtidas,comentarios,duracao_s,publicado,hook_falado,legenda,url
(use “?” em envios e publicado se não estiverem visíveis)

BLOCO 2 · JSON para o banco (um objeto por reel, para eu colar dentro da categoria certa em data/hooks.json):
{"cat": "VE", "t": "<template>", "e": "<hook_falado>", "p": "@criador · <views> views"}

Por último, me dê um RESUMO com:
- os 3 padrões de hook que mais se repetiram nos outliers
- 5 hooks novos para o meu nicho [NICHO] usando esses padrões, cada um com texto na tela (3 a 7 palavras) e primeiro frame sugerido
```

---

## Depois da mineração

1. Cole o **Bloco 1** no fim de `data/reels-minerados.csv`.
2. Cole cada objeto do **Bloco 2** dentro de `"hooks"` da categoria indicada em `data/hooks.json` (sem o campo `"cat"`).
3. Rode `python3 scripts/hooks.py build` para regerar a tabela.
