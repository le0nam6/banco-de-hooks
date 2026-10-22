# 12 · Outliers de outubro de 2026 (coleta pelo Claude in Chrome)

O Claude in Chrome abriu 82 Reels de 26 perfis brasileiros (Nigro, Benchimol, Toledo, Joel Jota, Caio Carneiro, Izabela Anholett, Fernando Miranda, @paulo.ia, Rony, Conrado Adolpho e outros) e devolveu três arquivos. Eles já estão no banco:

- `data/hooks.json`: 75 ganchos novos com prova (6 ficaram de fora por já existirem ou não terem fala). A marca é "out/2026 (Claude in Chrome)" no campo `p`.
- `data/reels-minerados.csv`: 58 Reels novos. Outros 24 já estavam lá com o endereço `/p/` em vez de `/reel/`, e o arquivo agora é deduplicado pelo código do post.
- `data/hooks-detalhados.csv`: a tabela completa de cada Reel, com texto na tela, primeiro quadro, fala, confirmação, foreshadow, CTA, categoria, template e o porquê de funcionar. É a parte mais útil para copiar a estrutura, porque mostra as quatro camadas do hook juntas.

## O que os 82 mostram

- **A confirmação vem logo depois do gancho em 79 de 82.** É quase regra: a segunda frase prova a primeira.
- **O foreshadow é opcional:** só 30 de 82 prometem o que vem no fim.
- **O gancho falado inteiro tem umas 22 palavras** (mediana), em duas frases. A regra de ~14 palavras vale para a primeira frase, não para o gancho inteiro.
- **Vídeo longo roda:** a duração mediana é 1min46. São 33 acima de 2 minutos e só 7 abaixo de 30 segundos.
- **Familiaridade está em quase todos:** Bolsa, Pix, Instagram, Messi, Real Madrid, Yakult, Casas Bahia, ChatGPT, copo Stanley, Tesla. Confirma o `10-familiaridade.md`.
- **A maioria abre com a pessoa falando para a câmera.** Quem não aparece precisa que o primeiro quadro seja a prova (o urso na sala do @paulo.ia, a foto do Messi bebê).

**Cuidado com a leitura por categoria.** Nessa amostra, número chocante, prova visual e história pessoal têm a maior mediana de views. Mas são 4 ou 5 vídeos cada, puxados por perfis gigantes (Nigro, Benchimol, @paulo.ia). Serve como pista, não como regra.

**O que faltou:** os envios vieram vazios ("?"). O perfil público não mostra envios, que é justamente o sinal mais forte para alcançar quem não segue. Para medir envio, só com os Insights de quem é dono do vídeo.

## Os que servem para um perfil de IA e marketing sem rosto

| Perfil | Padrão | Exemplo |
|---|---|---|
| @paulo.ia | Prova visual de IA no primeiro quadro, depois a promessa | "Hoje eu vou te ensinar a criar efeitos especiais com inteligência artificial. Sim, todas essas cenas foram criadas usando apenas IA." (13,3 mi) |
| @paulo.ia | Alerta protetor feito para mandar para a família | "Em 2026 vai ficar praticamente impossível saber o que é real ou não…" (30,5 mi) |
| @izabela.anholett | Notícia de IA com marca que o público usa | "O ChatGPT acabou de lançar uma atualização que pode ser o começo do fim dos empregos que a gente conhece…" (830 mil) |
| @fernandomiranda777 | Case de marca com pergunta ou contradição | "Como que é possível o Parque Ibirapuera faturar 160 milhões por ano se você entra de graça?" (799 mil) |
| @rafaelkiso | Confirma a suspeita de quem trabalha com Instagram | "O alcance orgânico do Instagram tá caindo sim." (113 mil) |

Coleta: Claude in Chrome, 18 e 19/10/2026. Views na data da coleta.
