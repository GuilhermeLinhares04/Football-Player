### 🧍 Criação e Personalização do Jogador

* Escolher nome, nacionalidade, idade, posição inicial
* Escolher quantidade de dinheiro inicial (baixo, médio, alto)
* Força inicial aleatória baseada na posição e idade
* Popularidade inicial aleatória (com base na popularidade do clube e nacionalidade)
* Escolher ano inicial da carreira
* Escolher personalidade (ou aleatória) que afeta atributos mentais, relações, popularidade e desenvolvimento
* Selecionar estilo de vida (básico, médio, alto)

---

### 📊 Atributos e Desenvolvimento

* Todos os atributos são medidos de 0 a 100 (inclusive times, nações e funcionários)
* Atributos principais: força, chute, cabeceio, etc.
* Atributos adicionais: técnica, posicionamento (goleiro e linha), passes longos e curtos, aptidão física, elasticidade
* Atributos mentais: determinação, inteligência, agressividade, liderança
* Treinamentos afetam atributos (foco de treino)
* Contratar personal trainers para acelerar desenvolvimento
* Atributos físicos diminuem com o avanço da idade
* Intensificadores ilegais (com riscos)

---

### Base de Dados (Todos os atributos são de 0 a 100)

* Clubes: id, nome, força, id nação, id liga, atributo finanças, atributo instalações, atributo popularidade
* Nações: id, nome, força, atributo popularidade, id do continente, atributo de dinamismo (feito para mudar formatos de competições da nação ou criar novas competições)
* Continentes: id, nome
* Competições: id, nome, atributo popularidade, número de clubes participantes, id do formato, id da nação (0 se for competição continental), id do continente (0 se for competição mundial)
* Patrocínio: id, nome, atributo finanças, atributo popularidade, área de atuação (esporte, moda, etc.)
* Empresários: id, nome, atributo finanças, atributo controvérsia, atributo negociação

---

### Formato de Competições (ser programado separadamente e com id para indicar na base de dados)

* Ligas:
    * Pontos corridos ida e volta
    * Pontos corridos apenas ida
    * Pontos corridos ida, volta e mais um turno
    * Pontos corridos ida e volta com playoffs ida e volta para decidir campeão
    * Pontos corridos apenas ida com playoffs para decidir campeão
    * Pontos corridos ida e volta com playoffs apenas ida para decidir campeão
    * Pontos corridos apenas ida com playoffs apenas ida para decidir campeão
    * Pontos corridos ida e volta seguido de fase de grupos (um grupo para decidir o campeão e outro para decidir rebaixamento)
* Copas:
    * Mata-mata (ida e volta)
    * Mata-mata (apenas ida)
    * Grupos com mata-mata (grupos ida e volta, mata-mata ida e volta e final em jogo único)
    * Grupos com mata-mata (grupos ida e volta, mata-mata ida e volta e final ida e volta)
    * Grupos com mata-mata (grupos apenas ida, mata-mata apenas ida)
    * Fase de liga com mata-mata (8 partidas na liga e final em jogo único)

---

### ⚽ Carreira e Jogo

* Time inicial baseado na nacionalidade (com chance de clube estrangeiro)
* Simulação por temporada com estatísticas: partidas, gols, assistências, nota média, desempenho do time
* Estatísticas específicas por posição (goleiro, zagueiro, lateral, etc.)
* Felicidade influencia desempenho
* Jogador pode requisitar:
  * Troca de posição
  * Mudança de time (empréstimo ou transferência)
  * Mudança de nacionalidade (para ser possível, precisa estar a um determinado tempo no país em questão)
* Premiações individuais com base em desempenho
* Convocações para seleções (sub-17, sub-20, sub-23 (Olímpiadas, com pequena chance de ser convocado com mais de 23 anos dependendo de sua força e popularidade), principal)
* Aposentadoria da seleção ou total
* Algoritmo de simulação:
  * Participação em jogos com base na relação com treinador e desempenho
  * Estatísticas baseadas nos atributos do jogador e força do time
  * Nota média impacta relação com o treinador
* Mostrar desempenho do clube em ligas, copas nacionais e internacionais
* Ano padrão da base de dados é 2025, caso seja escolhido um ano diferente, o jogo simula os anos restantes até 2025 (ex: se o jogador começa em 2020, o jogo simula o mundo do futebol 5 anos para chegar a 2025, ou se quiser começar em 2030, o jogo simula os anos de 2025 a 2030)
* Mundo do futebol evolui conforme o tempo passa:
  * Alteração de atributos dos clubes
  * Alteração de atributos das seleções
  * Alteração em competições (criação de novas competições, alteração de formato, etc.)

---

### 💼 Carreira Profissional e Finanças

* Receber propostas de:
  * Clubes (transferência ou empréstimo)
  * Patrocínios (com base na popularidade do jogador, estatísticas e estilo de vida)
* Gerenciar finanças:
  * Estilo de vida impacta gastos e popularidade
  * Receitas: salário, prêmios, patrocínios
  * Investimentos diversos
* Contratar empresários para obter melhores propostas
* Central de mensagens com ofertas e eventos

---

### 🤝 Relações e Vida Pessoal

* Relações com:
  * Treinador
  * Família
  * Namorada/noiva (se tiver)
  * Amigos
  * Patrocinadores
  * Torcida
  * Colegas de time
* Gerenciar tempo entre treino e relações (impacta felicidade e desempenho)
    * O jogador recebe um número de horas por dia para treinar e se relacionar, e o jogador pode escolher como dividir esse tempo entre treino e relações (ex: 4 horas de treino e 2 horas com a namorada ou 6 horas de treino e 0 horas com a namorada)
* Possibilidade de ter filhos com a namorada
* Felicidade afetada por salário, relações, estilo de vida, desempenho
* Família influencia decisões de carreira (mudança de clube, patrocínio)
* Namorada com atributos que impactam felicidade, gastos e popularidade (escândalo, oportunismo, amor, beleza)

---

### 📈 Popularidade e Reputação

* Popularidade inicial aleatória e evolutiva
* Afetada por desempenho, relações, estilo de vida, escândalos e clube
* Impacta propostas de patrocínio, convocações e transferências
* Relação com torcida afeta popularidade, desempenho e felicidade

---

### 💬 Interações e Sistema Social

* Central de mensagens com propostas e novidades
* Diálogos com treinador (pedir mais tempo, mudança de posição, renovação de contrato etc.)
* Relação com colegas de time (amizade, rivalidade, respeito), influencia na felicidade e desempenho
* Interações com torcedores (fotos, autógrafos, entrevistas)

---