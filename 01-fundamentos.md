# 01 · Fundamentos: por que um hook funciona

Antes de usar o banco, entenda as regras. O agente usa este arquivo para decidir **qual** hook usar e para **auditar** o que escreveu.

## 1. O que o Instagram mede (e o que o hook precisa mover)

| Sinal | O que é | Fonte | O que o hook faz por ele |
|---|---|---|---|
| **Taxa de pulo (skip rate)** | % de pessoas que passam o vídeo nos primeiros ~3 s | Insights do Reels | O hook existe para baixar esse número. |
| **Retenção aos 3 s** | % de quem ainda está assistindo no 3º segundo | Insights do Reels | Meta prática de Fernando Miranda: **nunca abaixo de 50%**. Vídeo viral costuma ter **skip rate abaixo de 30%**. |
| **Tempo de exibição** | Tempo assistido total e médio, incluindo replay | Adam Mosseri (Instagram), jan/2025 | Hook + foreshadow seguram, e o roteiro mantém. |
| **Envios por alcance** | Quantas pessoas mandaram o Reels por DM ÷ alcance | Mosseri, jan/2025 | É o sinal mais forte para alcançar **não seguidores**. |
| **Curtidas por alcance** | Curtidas ÷ alcance | Mosseri, jan/2025 | Mais relevante para quem já te segue. |

Regras práticas que saem daí:

- **Reels de até 3 minutos** entram na recomendação para não seguidores. Acima disso, segundo Fernando Miranda, o vídeo fica quase só na sua base.
- **Use Trial Reels** (testes mostrados só para não seguidores) para testar 2 ou 3 hooks do mesmo vídeo sem queimar o perfil.
- O algoritmo “não liga pra quantos seguidores você tem. Ele quer saber se o seu vídeo é bom” (Fernando Miranda). Na prática: **CTR (parar) + retenção + envio**.

## 2. O que a mineração mostrou (228 reels brasileiros reais)

Amostra: os reels de maior alcance de @fernandomiranda777, @thiago.nigro, @izabela.anholett, @marcelotoledo, @joeljota, @caiocarneiro, @nathfinancas, @rafaelkiso, @denerlippert e outros, mais buscas por legenda (“inteligência artificial”, “marketing”, “negócio”, “ChatGPT”, “você não sabia”). Os dados estão em [`data/reels-minerados.csv`](data/reels-minerados.csv).

| Padrão | Nos reels com 500 mil+ views (98) |
|---|---|
| Primeira frase com **número** | 26 de 98 |
| Primeira frase falando com **você** (você, te, seu, sua) | 26 de 98 |
| Primeira frase em forma de **pergunta** | 18 de 98 |
| Usa **“acabou de”** (notícia quente) | 18 de 98 |
| Abre com **“Galera”** (tom de conversa, padrão Nigro) | 16 de 98 |
| Tamanho mediano da primeira frase | **14 palavras** |

Duração × alcance na amostra (mediana):

| Duração | Reels | Views (mediana) | Envios (mediana) |
|---|---|---|---|
| até 30 s | 13 | 297 mil | 2,9 mil |
| 30–60 s | 39 | 283 mil | 2,7 mil |
| 60–120 s | 74 | 241 mil | 2,5 mil |
| 120–180 s | 74 | **487 mil** | **4 mil** |
| 180 s+ | 27 | 773 mil | 19 mil |

> Leitura honesta: a amostra tem viés (pegamos os melhores vídeos de perfis grandes). Mesmo assim, ela mostra que, **no Brasil, vídeos de história/análise de 1:30 a 2:50 com hook forte performam muito bem**. Não é verdade que “só vídeo curto viraliza”. Vídeo de até 30 s funciona quando é um aforismo que faz loop (Caio Carneiro, Joel Jota). Acima de 3 min, só se o perfil já é grande.

## 3. Os 4 componentes do hook (Kallaway)

Todo hook tem quatro camadas, que precisam apontar para a **mesma coisa**:

1. **Texto na tela.** É lido antes de tudo. Mais da metade das pessoas assiste sem som.
2. **Visual.** O que aparece no primeiro frame. Os olhos processam muito mais rápido que os ouvidos.
3. **Fala.** O que você diz.
4. **Áudio.** Música/efeito. Fernando Miranda usa música de suspense que termina com um “boom” quando o vídeo começa.

A ordem de leitura do cérebro é um sanduíche: **visual → áudio → visual**. A pessoa vê, ouve e volta a olhar para confirmar. Se o que ela ouviu não bate com o que vê, ela não entende e vai embora.

> “A diferença entre 500 e 500 mil views é o alinhamento máximo entre essas quatro coisas.” (Kallaway)

## 4. O motor de todo hook: contraste A → B

O hook abre um **loop de curiosidade** criando distância entre o que a pessoa acredita (**A**) e o que você mostra (**B**). Quanto maior a distância, maior a curiosidade.

- **Contraste explícito:** diz A e B. “Todo mundo acha que o Coco Bambu vende comida. Ele vende evento.” Use quando o público é amplo.
- **Contraste implícito:** diz só B e confia que o público conhece A. “O Dove é um detergente.” Use em nicho fechado.

Fernando Miranda chama isso de **dissonância cognitiva** ou **verdade escondida**: “Se não tem uma verdade escondida, o cara não para, porque é só notícia. Aí ele lê na Exame.”

Exemplo do próprio Fernando, ao rejeitar um hook:
- ❌ “A Zara vale bilhões sem nunca ter feito propaganda na TV.” (Técnico, e vale para muitas marcas. Não é contraintuitivo.)
- ✅ “O homem mais rico do Japão vende camiseta básica.” (Contradição imediata: rico × básico.)

## 5. A gramática de 6 peças (Kallaway)

`[Sujeito] + [Ação] + [Resultado] + [Contraste]` (+ `[Prova]`) (+ `[Tempo]`)

| Peça | Obrigatória? | Exemplo |
|---|---|---|
| Sujeito | Sim | “Esse cara”, “você”, “a Shopee” |
| Ação | Sim | “vendia”, “fatura”, “largou” |
| Resultado | Sim, quanto mais chocante melhor | “85 milhões esse ano” |
| Contraste | Sim | “até tomar um golpe de 16 milhões” |
| Prova | Em conteúdo educativo | “de novo”, número, print na tela |
| Tempo | Quando é crível | “em 90 dias”, não “rápido” |

Teste: “Esse cara vendia 300 carros por mês **[sujeito+ação+resultado]** até tomar um golpe de 16 milhões **[contraste]**. Mudou tudo e agora vai faturar 85 milhões **[resultado novo]** esse ano **[tempo]**.” (@fernandomiranda777)

## 6. Os 4 erros que matam um hook (Kallaway)

1. **Demora.** O tema aparece tarde. “Gente, isso é a coisa mais louca que eu já vi…” não diz nada. O tema precisa estar na primeira frase.
2. **Confusão.** Frase longa, jargão, voz passiva. Fernando cortou “arquitetura de consumo” e “matemática emocional” de um roteiro: “Fala a língua das pessoas.”
3. **Irrelevância.** A pessoa entende, mas não sente que é pra ela. Troque “eu sofri com X” por “se você sofre com X”. Mantenha o “eu” só quando a sua história *é* o gancho.
4. **Desinteresse.** É claro e relevante, mas não tem contraste. É o erro mais comum.

## 7. As duas razões para alguém enviar seu vídeo

Fernando Miranda: “Pra fazer uma pessoa compartilhar, ou você cria uma história inspiradora ou confirma uma suspeita.”

- **História inspiradora:** a pessoa manda “para puxar assunto” ou “para inspirar alguém” (categorias OR, HP, AF).
- **Confirmação de suspeita:** a pessoa usa você como argumento: “Viu? Eu falei.” (categorias SU, NQ, VE).

O Instagram está virando uma rede de DMs. O envio é a métrica que leva o vídeo para fora da sua bolha.

## 8. O hook é o programa, não só a frase

Fernando Miranda trata cada perfil como um **programa de TV** com formato fixo (como *O Aprendiz*, *MasterChef*, *BBB*):

- Promessa fixa: “Eu analiso as melhores estratégias de marketing do mundo todos os dias.”
- Fechamento fixo: “Meu nome é Fernando Miranda… se inscreve pra não perder a próxima.”
- Resultado: o público maratona (“tô no 10º vídeo seguido”) e quase todo vídeo performa, porque a audiência já sabe o que esperar.

Para o seu agente: **escolha 1 ou 2 categorias principais como formato do seu programa** e use as outras como variação.

## 9. Onde gastar o seu tempo

> “Se você tem um dólar pra gastar num texto, gaste 80 centavos no título.” (regra clássica do copywriting americano, citada por Fernando Miranda)

A maior parte das pessoas gasta tempo no meio e no fim do vídeo, que pouca gente vê. **Mais da metade do tempo de roteiro deve ir para os 3 primeiros segundos.** Fernando: “Até hoje eu não vi nenhum vídeo que foi bem no orgânico sem um hook muito bom.”
