# Shuffle-Game

O jogo foi criado com:
- *Python*3.6;
- *Pygame*;

![shuffle](https://temptempo.yolasite.com/resources/Shuffle%20-%20git.png)

## Funcionalidade
O *Shuffle* é um jogo em que o jogador vira as cartas de modo a juntar 1 par igual. 
- Quando o jogador combina o par certo o *score* aumenta 100 pontos.
- Quando o jogador combina o par errado, cada vez que que tenta combinar essas mesmas cartas, o *score* é diminuído.
A penalização do *score* aumenta de 20 em 20.

Após o jogador conseguir combinar todas as cartas, o nível termina e é desbloqueado o próximo nível.

Para os níveis mais avançados, existe um *timer*, existindo assim a possibilidade de perder o jogo.
- É possível perder o jogo nos níveis 5 e 5.1, caso o jogador deixe o *timer* chegar ao fim.
- Caso o jogador consiga combinar o par, ganha um bónus no *timer*.

---

## Estrutura do jogo
O código é constítuido por 13 ficheiros com 3 bibliotecas:
- *ex.py*;
- *button.py*;
- *variables.py*;
- *shuffle.png*;
- *NotoSans-Regular.ttf*;
- *button sound.ogg*;
- *menu song.ogg*;
- *level 1 song.ogg*;
- *level 2 song.ogg*;
- *level 3 song.ogg*;
- *level 4 song.ogg*;
- *level 5 song.ogg*;
- *level 5.1 song.ogg*;
- *pygame*
- *random*
- *time*

---

O *ex.py* contém as principais funções que correm o jogo.

O *button.py* contém as classes responsáveis pela criação das cartas e dos botões.

O *variables.py* contém variáveis essenciais para a maior parte dos níveis.

### Estrutura do código
O código está dividido em 4 principais funções, denominadamente *main()*, *menuScreen()*, *gamePlayEasyLevels()* e *gamePlayHardLevels()*.
Contém também a classe *Card* e a *child class* *Text* e uma função secundária *compare()*. 

---

#### *menuScreen()*

É responsável por executar o menu. Vai criar a imagem do jogo e os vários botões que dão acesso aos restantes níveis.

---

#### *gamePlayEasyLevels()*

Função que corre os níveis 1, 2 e 3. A função vai criar os botões de *help*, *exit* e listas com diferentes combinações randomizadas (formas e cores).

Para a criação, vai criar cartas com a classe *Card* em que vão ser definidas as suas posições, largura e altura e as restantes características.
De seguida, define o que acontece ao carregar nos botões ou as cartas.

Após isto, vai desenhar o *score*, o botão *exit*, a última carta *clicked* e o botão *help*. Vai também definir o que acontece quando o jogador vence o jogo.

Posteriormente, vai desenhar todas as cardas caso estejam *clicked* ou não. No caso terem sido *clicked*, em vez de desenhar a carta, vai desenhar a forma e cor que lhe foi atríbuida.

Quando existirem 2 cartas *clicked*, vai executar a função *compare* (*variables.py*) que compara a forma e a cor de ambas as cartas.

Após a função ser corrida vai retornar *True* ou *False*. Dependendo do seu retorno, caso seja *True*, vão ser eliminadas as cartas e o *score* é acrescentado; caso seja *False*, as cartas voltam a ser voltadas e o *score* é diminuído. 

---

#### *gamePlayHardLevels()*

Função que corre os níveis 4, 5 e 5.1.
A função é bastante semelhante à função *gamePlayEasyLevels()*.

Tem como principal diferença a criação dos níveis 5 e 5.1, em que foi implementado um *timer* e a forma como as cartas são desenhadas.

Nestes níveis as cartas são desenhadas enquanto andam para baixo ou para cima. Quando o jogador compara o par certo o *timer* reduz.

---

#### *main()* 

É responsável por executar as restantes funções.

---

#### *compare()*

Recebe 2 parâmetros e compara a forma e a cor que lhes foram atribuídos.

---

#### *Card*

A classe contém a posição, a largura e altura, o *score* (serve para ver quantas vezes foi *clicked*) e variáveis que definem se foi *clicked*, se pode ser *clicked* ou está a ser *clicked*.

Contém os métodos *isAt*, *draw*, *form* e *smallForm*.

O *isAt* é responsável por retornar a posição da carta.

O *draw* é responsável por desenhar a carta.

O *form* é responsável por desenhar a forma e cor da carta, juntamente com a sua *border*.

O *smallForm* é semelhante ao *form* mas para as cartas mais pequenas.

---

#### *Text (Card)*

É responsável pela criação de botões com texto.

----

## Conclusão

Durante o desenvolvimento do projecto, surgiram várias dificuldades, contudo, consegui ultrapassar as mesmas chegando ao objectivo final. Este projecto, apesar de pequeno e não ter um elevado nível de complexidade, ajudou-me bastante a desenvolver a compreensão de *Python* a compreender a estrutura de um pequeno jogo como o *Shuffle*.

---

Pedro Marques, 21900253
