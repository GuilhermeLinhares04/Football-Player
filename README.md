# Football-Player
Text-based football player career simulator

Funcionalidades atuais e futuras:
- Escolher nome do jogador, nacionalidade, idade, posição inicial e quantidade de dinheiro inicial (pequeno, médio ou baixo)
- Força inicial escolhida aleatoriamente, com base na posição escolhida e na idade inicial
- Popularidade escolhida aleatoriamente no início
- Ano inicial pode ser escolhido pelo jogador
- Time inicial é escolhido com base na força inicial e a nacionalidade inicial, com uma pequena chance de ser um clube do exterior
- Escolher foco dos treinos (força, chute, cabeceio, e o que mais achar relevante para a posição), isto afetar no aumento ou diminuição da força ao decorrer das temporadas
- O usuário avança um ano na carreira do jogador e uma tabela com estatísticas é mostrada para ele após o fim de certo ano, com número de partidas, gols, assistências, nota média e o desempenho dos times nas competições (lembrando que tudo isso é simulado com base na força do time e do jogador criado)
- A cada fim de temporada também, é mostrado um quadro de proposta de outros times, seja de empréstimo ou transferência, claro com base nas estatísticas do jogador, na sua força atual e na sua popularidade
- Opção para escolher estilo de vida (básico, médio ou alto) que afetará na quantidade de dinheiro do jogador e também na sua popularidade
- Relações do jogador com treinador, amigos (aleatório quando iniciar a carreira), namorada ou noiva (se ou quando tiver), patrocinadores, treinador da seleção e família
- Jogador pode receber propostas de patrocínio com base na sua popularidade, e estas ajudam a obter mais dinheiro
- Com base na sua força e popularidade, o jogador pode ser chamado para representar sua seleção e suas estatísticas também são mostradas ao fim das temporadas.
- Opção de se aposentar ou se aposentar apenas da seleção
- A força do jogador diminui enquanto ele fica mais velho, logicamente
- Base de dados com informações necessárias para times, seleções, patrocínios, competições e o que achar necessário <br>
~~- Situações que afetam atributos, popularidade e relações~~ (pode ficar muito repetitivo)
- Gerenciar tempo com relações (namorada, amigos, família e treino do time)
- Se o jogador tiver namorada, ele pode começar tentar engravidá-la e ter filhos
- Caso o jogador invista muito tempo no seu treino, por exemplo, ele pode ter problemas com a namorada, amigos e família, o que pode afetar na sua felicidade. O mesmo acontece se ele investir muito tempo com a namorada, amigos e família, seu treinador pode não gostar e isso afetar no seu desempenho em campo
- A família é importante quando um jogador decidir aceitar uma proposta de patrocínio ou ir a outro clube
- Barra de felicidade do jogador que também influencia em seu desempenho em campo. Ela pode ser afetada pelo seu salário, relações e outros
- Adicionar atributos do jogador para dar norte à escolha dos treinos
- Premiações individuais a cada fim de temporada, com base no seu desempenho e popularidade
- Investimentos para administrar o dinheiro
- Comprar empresários e personal trainers, para receber boas propostas e melhorar sua força geral
- Seleções sub-20, sub-17 e sub-23 (olímpiadas)
- Central de mensagens para receber propostas de times, patrocínios, seleções e outras informações
- Escolher personalidade do jogador (ou ser aleatória), que afetará em seus atributos mentais, relações, popularidade e desenvolvimento
- Instalaçoes dos clubes influenciam no desenvolvimento do jogador
- Atributos da namorada, como escândalo, oportunismo, amor, beleza, que afeteam na popularidade, felicidade do jogador e também seus gastos
- Gestão de finanças do jogador, com gastos de estilo de vida, investimentos, salário, prêmios e patrocínios
- Jogador pode requisitar troca de posição
- Jogador pode requisitar mudança de nacionalidade
- Jogador pode requisitar mudança de time, seja por empréstimo ou transferência
- Algoritmo de simulação de temporadas:
    - A simulação do número de partidas jogadas deve ser feita com base na relação inicial do jogador com o treinador. Inicialmente, o jogador deve ter uma chance menor de participar de cada partida, já que é jovem e sua força não é tão grande. A cada temporada, essa chance deve aumentar ou diminuir com base no desempenho do jogador e na relação com o treinador
    - A simulação das estatísticas do jogador deve ser feita com base nos atributos do jogador e a força do time. Por exemplo, se o jogador tem um atributo de finalização alto, ele deve ter uma chance maior de marcar gols. Se o time do jogador é fraco, ele deve ter menos chances de marcar gols e mais chances de sofrer gols	
    - A simulação da nota média deve ser feita com base nas estatísticas do jogador de acordo com sua posição
    - Felicidade do jogador afeta no desempenho das partidas, quanto mais feliz, melhor pode ser seu desempenho
    - Quanto maior a nota média, maior a relação com o treinador e consequentemente maior a chance de ser participar de mais partidas
    ### Estatísticas por Posição

    Para tornar a simulação mais realista, podemos adicionar estatísticas específicas para cada posição. Aqui estão algumas sugestões:

    #### Goleiro
    - Defesas realizadas
    - Gols sofridos
    - Jogos sem sofrer gols
    - Penalidades defendidas
    - Saídas do gol bem-sucedidas

    #### Zagueiro
    - Desarmes realizados
    - Interceptações
    - Cortes de bola
    - Gols marcados
    - Assistências
    - Faltas cometidas

    #### Lateral
    - Desarmes realizados
    - Interceptações
    - Cruzamentos bem-sucedidos
    - Assistências
    - Gols marcados
    - Passes precisos

    #### Meio-campista
    - Passes precisos
    - Assistências
    - Gols marcados
    - Desarmes realizados
    - Interceptações
    - Dribles bem-sucedidos

    #### Ponta
    - Assistências
    - Gols marcados
    - Cruzamentos bem-sucedidos
    - Dribles bem-sucedidos
    - Passes precisos

    #### Atacante
    - Gols marcados
    - Assistências
    - Finalizações no alvo
    - Dribles bem-sucedidos
    - Faltas sofridas
    - Impedimentos

    Essas estatísticas ajudarão a fornecer uma visão mais detalhada do desempenho do jogador em sua posição específica.
- Mais atributos a adicionar: Técnica, dividir entre posicionamento do goleiro e posicionamento em campo, dividir em passes longos e passes curtos, aptidão física, elasticidade (para goleiros)
- Atributos mentais: Determinação (depende das relações do jogador), inteligência, agressividade (afeta na nota média), liderança (chance de ser capitão)
- Opção para utilizar intensificadores ilegais para melhorar atributos do jogador, mas com riscos de ser pego e punido
- Mostrar desempenho do time do jogador em competições, como a liga nacional, copas nacionais e internacionais