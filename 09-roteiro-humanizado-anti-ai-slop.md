# 09 · Roteiro humanizado (anti-AI slop)

Roteiro com cara de IA perde a pessoa no segundo 2. Ela não sabe explicar o porquê, mas sente que é texto de máquina e rola o feed. Este arquivo é o filtro que o agente passa em **todo** hook e roteiro antes de entregar.

> Por que isso pesa no alcance: o Instagram vem dizendo que quer premiar conteúdo humano e original. Segundo análises do memorando de fim de ano de Adam Mosseri (dez/2025), a prioridade em 2026 é “conteúdo cru e real” em vez de material gerado por IA. Na prática, roteiro genérico derruba a retenção, e retenção é o que distribui o vídeo.

O gabarito de “como brasileiro fala num vídeo que performa” são as transcrições reais em [`data/reels-minerados.csv`](data/reels-minerados.csv). Quando estiver em dúvida, leia 5 linhas dali em voz alta e compare.

---

## 1. Lista negra: palavras e expressões que entregam IA

Se aparecer no roteiro, troque. Se não tiver troca, corte.

| Cara de IA | Troca por (ou corte) |
|---|---|
| “Mergulhar em”, “vamos mergulhar” | “Vou te mostrar”, “olha só” |
| “Desvendar”, “desvendando os segredos” | “Descobrir”, “o que ninguém te conta” |
| “No cenário atual”, “no mundo de hoje”, “nos dias de hoje” | Corte. Ou diga a data: “esse ano”, “agora em outubro” |
| “Em um mundo cada vez mais…” | Corte a frase inteira |
| “É importante ressaltar que”, “vale destacar que”, “cabe mencionar” | Corte. Fale o fato direto |
| “Não é apenas X, é Y”, “não se trata só de X” | Use uma vez por vídeo, no máximo. Prefira “Ele não vende X. Vende Y.” |
| “E o melhor?”, “E sabe o que é mais incrível?” | “Só que tem mais”, ou corte |
| “Spoiler:”, “Plot twist:” | “Só que…”, “Até que…” |
| “Imagine…” abrindo o vídeo | Mostre a cena: “Você entra no restaurante e…” |
| “Potencializar”, “alavancar”, “otimizar”, “maximizar” | “Aumentar”, “melhorar”, “vender mais” |
| “Jornada”, “trajetória”, “ecossistema”, “sinergia” | “Caminho”, “história”, ou o nome concreto da coisa |
| “Transformador”, “revolucionário”, “disruptivo”, “game changer” | O número ou o fato que prova. Se não tem prova, corte |
| “Crucial”, “fundamental”, “essencial”, “primordial” | Corte o adjetivo. Mostre por que importa |
| “Robusto”, “abrangente”, “holístico”, “estratégico” (como enfeite) | Corte |
| “Destravar”, “desbloquear o potencial” | “Começar a vender”, “sair do lugar” |
| “Insights valiosos”, “dicas valiosas” | “O que funcionou”, “o que eu aprendi” |
| “Prepare-se para…”, “Fique ligado para…” | “Fica até o final que…” |
| “Neste vídeo, vamos explorar…” | Corte. Comece pelo hook |
| “Em resumo”, “Concluindo”, “Em suma” | Corte. Termine logo depois da entrega |
| “Você já parou para pensar que…?” | Afirme o fato. Pergunta só se for provocativa de verdade |
| “Afinal, …” fechando a frase com moral genérica | Corte, ou troque por uma lição concreta do case |
| “Sem mais delongas” | Corte |
| “Incrível”, “surpreendente”, “fascinante” em todo parágrafo | Uma palavra de espanto por vídeo, e brasileira: “insano”, “sinistro”, “bizarro” |
| Pronome “ele/ela” formal para marca (“a empresa, por sua vez,”) | Fale o nome de novo, como na conversa |
| Português de Portugal ou formal: “estás”, “irá realizar”, “efetuar” | “Tá”, “vai fazer”, “fazer” |

## 2. Padrões de estrutura que entregam IA

Palavra a gente troca fácil. Estrutura é o que mais denuncia.

| Padrão | Como aparece | Conserto |
|---|---|---|
| **Tudo em três** | “Rápido, simples e eficiente.” Toda lista com 3 itens, todo adjetivo em trio | Varie: 1 item forte, ou 2, ou 4. O Fernando reduz a 3 quando a lista é grande demais. Não infla de 1 para 3 |
| **Frases do mesmo tamanho** | Todas com 15 a 20 palavras, mesmo ritmo | Misture: frase longa, frase curta. Uma palavra. “48 horas. 48 horas.” |
| **Pergunta retórica + resposta** | “O resultado? Incrível.” “O segredo? Consistência.” | No máximo uma vez por roteiro. Em geral, afirme direto |
| **Contraste negativo em série** | “Não é sobre X. Não é sobre Y. É sobre Z.” | Um contraste por vídeo. Use o do hook |
| **Abertura de redação** | “A inteligência artificial tem transformado o marketing.” | Comece pelo fato específico: “A Meta acabou de liberar…” |
| **Fecho motivacional genérico** | “Lembre-se: o sucesso é uma jornada.” | Lição presa no case: “Chegar primeiro cria manchete. Continuar melhor cria mercado.” |
| **Travessão em toda frase** | “Ele vendeu tudo — e ganhou mais.” | Em roteiro falado, troque por ponto ou vírgula. Fala não tem travessão |
| **Adjetivo empilhado** | “Uma estratégia poderosa, inovadora e eficaz” | Um substantivo concreto + um número |
| **Abstração** | “O poder da marca pessoal” | Cena: “O Ronaldo começou a me seguir depois desse vídeo” |
| **Neutralidade em cima do muro** | “Há prós e contras, depende do contexto” | Tome posição. Hook bom tem opinião |
| **Sujeito vago** | “Tem empresa pagando caro…”, “Muita gente acha que…”, “Tão vendendo isso como…”, “Tem gente que…” | Diga quem: o nome, a marca, “o seu banco”, “o cara da agência que te ligou”. Se não dá pra dizer quem, a afirmação não tem prova: corte |
| **Tudo bonito e limpo demais** | Zero hesitação, zero gíria, zero “né” | Deixe uma marca de fala: “tá?”, “olha só”, “pô”, “cara” |
| **Emoji e hashtag na fala** | Roteiro com 🚀 e #marketing | Emoji é para legenda, não para roteiro |
| **Frase cortada pra caber no tempo** | “Quando você monta o móvel, você gosta mais dele, mesmo meio torto.” Palavras tiradas só pra bater o limite de segundos | Fale a frase inteira, como no áudio de WhatsApp: “Quando você mesmo monta o móvel, você gosta mais dele, mesmo ele ficando meio torto.” Se estourou o tempo, corte uma ideia inteira, nunca as palavras de ligação |
| **Ditado inventado no fim** | “E nome que você escolheu, você fala.” Frase com cara de provérbio que afirma uma coisa absoluta | Diga do jeito que a prova sustenta: “você tem mais probabilidade de falar”. Aforismo absoluto soa a IA e promete mais do que o estudo mostra |
| **Confirmação seca depois do gancho** | “É o Nubank.” | Fale como quem responde a curiosidade de alguém: “Sim, estamos falando do Nubank.” |

## 3. Regras de oralidade brasileira

Tiradas dos reels minerados. Siga isto e o roteiro soa falado.

1. **Contração sempre.** “Tá”, “pra”, “pro”, “cê” (com moderação), “tô”, “num” (“num restaurante”).
2. **Abertura de conversa.** “Galera”, “Olha só”, “Pô, galera”, “É, galera”. É o padrão do @thiago.nigro: 16 dos 98 vídeos acima de 500 mil views da amostra abrem com “Galera”.
3. **Repetição proposital para fixar.** “Apodrece em 48 horas. 48 horas. Dois dias.” (@gzhdigital · 443 mil views)
4. **Chamada no meio da frase.** “…e o campo de batalha é o seu rosto, tá?” (@izabela.anholett · 3 mi views)
5. **Interjeição de espanto brasileira.** “Insano”, “sinistro”, “bizarro”, “olha que loucura”, “deu uma surra”.
6. **“Você” o tempo todo.** “Se você já entrou no Morumbi… você deixou dinheiro no bolso do mesmo cara.” (@fernandomiranda777)
7. **Número falado do jeito que se fala.** “Quase 2 mil”, “uns 7 mil reais”, “300 reais”. Nunca “R$ 287,90”.
8. **Frase incompleta é permitida.** “Mais ou menos.” “Pois é.” “Até que…”
9. **Referência local.** Bairro, cidade, estado, novela, time, grupo da família no WhatsApp, Pix, iFood.
10. **Humor de canto de boca.** “Beijo, Cariani.” “Eu não queria o óculos laranja, mas virou marca.” Uma por vídeo humaniza.
11. **Admitir o limite.** “Eu não sei se isso vai funcionar pra você.” “Eu errei feio aqui.” Máquina não admite erro.
12. **Teste do WhatsApp:** você mandaria essa frase num áudio pra um amigo? Se não, reescreva.

## 4. Antes e depois

**Hook**

> ❌ IA: “Descubra como a inteligência artificial está revolucionando o marketing digital e transformando a maneira como as empresas se conectam com seus clientes.”
>
> ✅ Humano: “A Meta acabou de liberar uma IA que monta a campanha inteira sozinha. E o gestor de tráfego que só aperta botão vai sumir.”

O que mudou: fato específico com nome próprio, verbo “acabou de”, contraste e consequência para uma pessoa real. Saíram “descubra”, “revolucionando”, “transformando” e “se conectam”.

**Trecho de case**

> ❌ IA: “O Coco Bambu é um exemplo fascinante de como a experiência do cliente pode ser um diferencial competitivo. Não se trata apenas de comida, mas de criar momentos memoráveis. Ambiente acolhedor, porções generosas e atendimento excepcional: essa é a fórmula do sucesso.”
>
> ✅ Humano (reescrita de Fernando Miranda): “O Coco Bambu não vende comida. Ele vende evento. Luz quente, pé-direito alto, madeira escura. Tudo pra você sentir que não é um jantar, é uma ocasião. E quando o seu cérebro acha que é uma ocasião, você aceita pagar 300 reais num prato.”

O que mudou: saíram o “exemplo fascinante”, o “não se trata apenas de” e o trio de adjetivos. Entraram a afirmação seca, os detalhes que dá pra ver e o número em reais.

**Fechamento**

> ❌ IA: “Em resumo, investir em conteúdo de qualidade é essencial para o sucesso a longo prazo. Lembre-se: consistência é a chave! 🚀”
>
> ✅ Humano: “Você que já foi no Coco Bambu: vale o preço? Comenta aí que eu quero ver a briga.”

**Correção do condutor (Nubank Parque, 20/10/2026)**

> ❌ Versão do agente: “É o Nubank, no estádio do Palmeiras.” / “Quando você monta o móvel, você gosta mais dele, mesmo meio torto.” / “Quem votou ajudou a montar. E nome que você escolheu, você fala.”
>
> ✅ Versão do Leonam: “Sim, estamos falando do Nubank, no estádio do Palmeiras.” / “Quando você mesmo monta o móvel, você gosta mais dele, mesmo ele ficando meio torto.” / “Quem votou ajudou a construir aquilo. E um nome que você mesmo escolheu, você tem mais probabilidade de falar.”

O que mudou: as frases voltaram a ser inteiras (o agente tinha cortado palavras para caber em 50 segundos e o texto ficou telegráfico), entrou o “você mesmo” de quem fala com alguém, e o fim deixou de ser um ditado absoluto para dizer só o que o estudo sustenta.

## 5. Como usar IA sem gerar slop

Fernando Miranda escreve os roteiros com uma IA no Claude, treinada nos vídeos mais virais dele, e mesmo assim revisa tudo à mão. Na gravação com Dener Lippert, ele apagou dois termos inventados pela IA e reescreveu metade do texto. O processo:

1. **Comece por material humano.** Uma história que você ouviu, um dado real, um print, um áudio seu explicando o tema. Nunca um prompt vazio do tipo “faça um roteiro sobre X”.
2. **Dê exemplos reais de ritmo.** Mande para o agente de 3 a 5 transcrições do `reels-minerados.csv` do mesmo formato e peça para imitar o ritmo, não o conteúdo.
3. **A IA estrutura, você dá a voz.** Peça estrutura (hook, confirmação, viradas, lição) e depois troque as frases para o seu jeito de falar.
4. **Leia em voz alta.** Se você tropeçar ou se sentir apresentador de telejornal, a frase está escrita, não falada.
5. **Passe o filtro deste arquivo** (seção 6). Se quiser um segundo passe, rode a skill `humanizer`.
6. **Grave com o texto como guia, não como prisão.** Pode mudar palavra na hora. O improviso pequeno é o que deixa humano.

## 6. Checklist anti-slop (o agente roda em todo roteiro)

Reprova se marcar **2 ou mais**:

- [ ] Tem alguma palavra da lista negra (seção 1)?
- [ ] Tem lista ou adjetivos em trio sem necessidade?
- [ ] Tem mais de uma pergunta retórica seguida de resposta (“O resultado? X.”)?
- [ ] Tem “não é X, é Y” mais de uma vez?
- [ ] As frases têm quase todas o mesmo tamanho?
- [ ] Abre com frase genérica que serviria para qualquer vídeo do nicho?
- [ ] Fecha com moral motivacional genérica?
- [ ] Não tem nenhum nome próprio, número ou lugar concreto?
- [ ] Tem sujeito vago (“tem empresa”, “muita gente”, “tão vendendo”) no lugar de quem fez de verdade?
- [ ] Não tem nenhuma contração (“tá”, “pra”) nem marca de fala?
- [ ] Tem travessão, emoji ou hashtag no texto falado?
- [ ] Fica em cima do muro, sem opinião?
- [ ] Você não mandaria isso num áudio de WhatsApp?

## 7. Prompt do passe anti-slop

O agente pode usar este prompt em si mesmo, ou você pode colar em qualquer IA depois de ter o rascunho:

```text
Revise este roteiro de Reels em português do Brasil para soar 100% falado por um brasileiro, sem cara de IA.

Regras:
1. Mantenha o significado, os fatos e os números. Não invente nada.
2. Corte ou troque: mergulhar, desvendar, no cenário atual, é importante ressaltar, não é apenas X é Y (deixe no máximo 1), E o melhor?, Spoiler, Imagine, potencializar, alavancar, jornada, ecossistema, revolucionário, transformador, crucial, essencial, insights valiosos, em resumo.
3. Quebre trios de adjetivos e listas de 3 que foram infladas.
4. Varie o tamanho das frases: algumas bem curtas. Pode repetir uma frase curta para dar ênfase.
5. Use contrações (tá, pra, pro, tô) e no máximo 2 marcas de fala (olha só, pô, cara, galera, tá?).
6. Nenhum travessão, emoji ou hashtag no texto falado.
7. Nível de leitura de uma criança de 11 anos. Voz ativa.
8. Final logo depois da entrega, sem moral genérica.

Devolva:
- o roteiro revisado
- uma lista curta do que você trocou e por quê
- nota de 0 a 10 de “soa humano” e o que ainda falta para chegar a 10

Roteiro:
[COLE AQUI]
```
