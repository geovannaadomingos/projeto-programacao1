# `Fazendinha CIn`

Fazendinha CIn é um projeto feito para aplicar os conceitos e conteúdos vistos durante a disciplina de Programação 1, do Centro de Informática([CIn](https://portal.cin.ufpe.br/)) da Universidade Federal de Pernambuco([UFPE](https://www.ufpe.br)). 

Nesse repositório, é possível encontrar os códigos desenvolvidos ao decorrer do processo e também informações relevantes sobre ele, como a organização dos arquivos, divisão de tarefas, tecnologias utilizadas, etc.   


------


## `Tecnologias utilizadas`

Essas foram as principais tecnologias utilizadas no desenvolvimento do projeto:

| Ferramenta | Descrição | Justificativa para o uso |
| --- | --- | --- |
| `Python` | Linguagem de programação | É uma linguagem legível, de fácil manutenção e que possibilita a reutilização de códigos. Além disso, roda em diferentes sistemas operacionais e possui diversas bibliotecas. |
| `Pygame` | Biblioteca de jogos baseada em Python | É uma biblioteca que nos permite, por meio do Python, criar jogos, já que fornece métodos prontos que facilitam o desenvolvimento. Assim, é possível renderizar imagens, definir larguras e comprimentos para o display, controlar o tempo, etc. |
| `Git` | Software de controle de versões | É um software que nos permite salvar e controlar versões desenvolvidas do nosso projeto. Ele possibilita a criação de espaços(branchs) de atuação para cada funcionalidade ou membro diferente da equipe, o que permite uma maior agilidade. |


------


## `Conceitos vistos na disciplina e aplicados no projeto`

Esses foram os principais conceitos vistos na disciplina de Programação 1 e aplicados no projeto:

| Conceito | Local onde foi utilizado |
| --- | --- |
| `Programação Orientada a Objetos` | A maior parte dos arquivos do projeto possuem classes, as quais representam objetos do mundo real e que possibilitam a aplicação de hierarquias, bem como a reutilização de códigos. Um exemplo disso é a classe GameObject, que representa um objeto gráfico genérico do jogo e que, por isso, outros objetos, como o regador(WateringCan), derivam dela. |
| `Laços de Repetição` | Um exemplo de arquivo em que laços de repetição são utilizados, mais especificamente o while, é o arquivo Main. Nesse arquivo, que é o arquivo principal do projeto, enquanto o projeto estiver rodando, o display é atualizado seguindo uma largura e uma altura. |
| `Estruturas Condicionais` | As estruturas condicionais também foram utilizadas em diversos locais do projeto. Um exemplo de arquivo onde isso acontece é o plantation, arquivo que contém a classe da plantação, na qual a evolução das plantas e suas respectivas imagens são controladas graças às condicionais. |
| `Listas e Dicionários` | Um dos arquivos que utiliza listas e dicionários é o relatório para o usuário(report). Nele, conseguimos armazenar quantas plantas(apresentadas no dicionário) o usuário coletou e, consequentimente, identificar se ele atingiu a meta daquele level. |
| `Funções e métodos` | Assim como o conceito de POO, as funções também foram utilizadas na maioria dos arquivos. Um dos arquivos em que a utilização de funções é mais recorrente é o arquivo farmer, que representa o fazendeiro e player do jogo. Diante disso, as ações dele, de andar, arar a terra, colher planta, etc., são representadas por funções. |


------


## `Instruções para executar o arquivo e jogar`
* Instale o Python a partir da versão 3.6, [seguindo a documentação oficial](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository) 
* Instale o Pygame, [seguindo a documentação oficial](https://www.pygame.org/download.shtml)
* Clone o projeto em sua máquina, [seguindo essas instruções](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository)
* Execute, utilizando linha de comandos, o arquivo main.py do projeto-programacao1
* Comece a jogar utilizando o seu mouse 


------


## `Arquitetura e organização dos arquivos`

```
 📁 projeto-programacao1
   |
   |-  📁 MainMenu
   |     |- 📄 game.py
   |     |- 📄 menu.py
   | 
   |-  📁 assets
   |     |- 📁 Sounds
   |     |- 📁 sprites
   |     |- 📄 Kenney Blocks.ttf
   |     |- 📄 LogoMenu-removebg-preview (1).png
   |     |- 📄 TELAA.png
   |     |- 📄 fonte.ttf
   |     |- 📄 logo.png
   |     |- 📄 telaredd.png
   | 
   |-  📁 data
   |     |- 📁 levels
   |     |- 📄 levels.json
   |     |- 📄 plants.json
   |  
   |   📄 .gitignore
   |   📄 Events.py
   |   📄 LICENSE
   |   📄 NodeState.py
   |   📄 README.md
   |   📄 datamanager.py
   |   📄 farmer.py
   |   📄 gamemanager.py
   |   📄 gameobject.py
   |   📄 hud.py
   |   📄 inventary.py
   |   📄 item.py
   |   📄 main.py
   |   📄 mouse.py
   |   📄 pathfinding.py
   |   📄 place.py
   |   📄 plantation.py
   |   📄 report.py
   |   📄 soundEffects.py
   |   📄 test.py
   |   📄 tilemap.py
   |   📄 tilemapEditor.py
   |   📄 vector2.py
   |   📄 waterWell.py
   |   📄 wateringCan.py
   |

```
Descrição dos arquivos:
* `MainMenu:` Pasta que contém objetos, com seus atributos e métodos, do menu do jogo
* `assets:` Pasta mídias(sons, imagens, fontes, logo, etc.) do jogo 
* `data:` Pasta que contém arquivos em json e dados(como de levels e estados das plantas) utilizados no jogo
* `.gitignore:` Arquivo que permite ignorar alguns arquivos, como de cache, etc., durante o versionamento
* `Events.py` Descrição
* `LICENSE:` Arquivo que contém a licença do projeto
* `NodeState.py:` Descrição
* `README.md:` Arquivo que contém descrições e informações relevantes do projeto em markdown
* `datamanager.py:` Descrição
* `farmer.py:` Arquivo que contém os métodos e atributos do objeto fazendeiro (player)
* `gamemanager.py:` Descrição
* `gameobject.py:` Descrição
* `hud.py:` Arquivo que contém a interface do relatório, pontuando quantas plantas foram colhidas, para o player
* `inventary.py:` Arquivo que contém os objetos coletados pelo usuário durante o jogo
* `item.py:` Descrição
* `main.py:` Arquivo principal, que contém a intância de todos objetos utilizados no jogo, e que deve ser executado para jogar
* `mouse.py:` Descrição
* `pathfinding.py:` Descrição
* `place.py:` Arquivo que contém o objeto de lugar, uma classe genérica da qual outras classes que representam lugares no jogo vão derivar (exemplo: poço)
* `plantation.py:` Arquivo que contém os métodos e os atributos da plantação
* `report.py:` Arquivo que a classe que recebe informacões sobre os objetos coletados e manipulados pelo player
* `soundEffects.py:` Arquivo que contém manipulação de sons do jogo
* `test.py:` Arquivo que serve para rodar testes durante o desenvolvimento
* `tilemap.py:` Descrição
* `tilemapEditor.py:` Descrição
* `vector2.py:` Descrição
* `waterWell.py:` Arquivo que contém a classe do espaço poço, seus atributos e métodos
* `wateringCan.py:` Arquivo que contém a classe do objeto regador, seus atributos e métodos


------


## `Dificuldades enfrentadas`

Ao decorrer da idealização e do desenvolvimento do projeto, algumas dificuldades foram enfrentadas, mas, a partir disso, algumas lições foram aprendidas, conforme os tópicos a seguir:

* `Maior erro enfrentado e como lidamos com ele:` Estabelecemos muitas features para o projeto, mas não priorizamos e nem levamos em consideração os requisitos básicos propostos pelos orientadores. Nesse contexto, com um pouco menos de tempo para o desenvolvimento, percebemos isso e nos reunimos para mudar o escopo, cumprindo primordialmente os requistos básicos e deixando outras features em stand by. Dessa forma, foi possível garantir o básico e, somente assim, partir para o mais complexo.
* `Maior desafio enfrentado e como lidamos com ele:` A maior parte da equipe nunca tinha feito interfaces 2D utilizando Python. Diante disso, concordamos em, individualmente, antes de desenvolver o projeto, fazer um pequeno jogo, similar ao jogo [Flappy Bird](https://flappybird.io/), a fim de que todos passassem a ter essa noção básica de como criar tais interfaces. A partir daí, tornou-se um pouco mais simples o desenvolvimento dos códigos ao longo do projeto.
* `Lições aprendidas durante o projeto:` Dentre tantos conceitos técnicos estudados e aplicados, também foi possível aprender sobre a necessidade de priorizar tarefas, de respeitar os pré-requisitos para o desenvolvimento e de enxergar a importância da organização e do planejamento antes do "mão na massa". Além disso, vimos o quanto o trabalho em equipe e o apoio mútuo são fundamentais para enfrentar dificuldades e desafios que surgem ao longo de qualquer projeto de desenvolvimento.


------


## `Divisão de tarefas`

O gerencimento de atividades foi feito utilizando a ferramenta [Trello](https://trello.com/pt-BR). De maneira geral, a execução de atividades se deu da seguinte forma:

* `Demetriu Gabriel:` class Plantation(plantação), class Inventary(Inventário)
* `Geovanna Domingos:` Auxílio com git e github, class WateringCan(Regador), class WaterWell(Poço), class Report(relatório para o usuário) e README.md
* `Giovanna Machado:` Menu
* `José Luiz:` SoundEffects
* `Luana Brito:` Pathfinding e Hud report (Interface do relatório para usuário, pontuando objetos coletados)
* `Lucas Campos:` Auxílio com Python e Pygame, Farmer(fazendeiro player) TileMap(imagens, interfaces gráficas e cenários do jogo), criação dos arquivos e classes mais gerais(test, main, gamemanager, gameobject, mouse, vector2, place e item)


------


## `Autores do projeto`

Esse é o time de alunos, da graduação em Sistemas de Informações, responsável pela idealização e desenvolvimento do projeto:

| [<img src="https://avatars.githubusercontent.com/u/53124770?v=4" width=115><br><sub>Geovanna Domingos</sub>](https://github.com/geovannaadomingos) |  [<img src="https://avatars.githubusercontent.com/u/104396639?v=4" width=115><br><sub>Luana Brito</sub>](https://github.com/LuanaCCBrito) |  [<img src="https://avatars.githubusercontent.com/u/104479818?v=4" width=115><br><sub>José Luiz</sub>](https://github.com/jldsn) |
| :---: | :---: | :---:
| [<img src="https://avatars.githubusercontent.com/u/34292933?v=4" width=115><br><sub>Lucas Campos</sub>](https://github.com/lucasccampos) |  [<img src="https://avatars.githubusercontent.com/u/54682631?v=4" width=115><br><sub>Demetriu Gabriel</sub>](https://github.com/DemetriuGabriel) |  [<img src="https://avatars.githubusercontent.com/u/86128256?v=4" width=115><br><sub>Giovanna Machado</sub>](https://avatars.githubusercontent.com/u/86128256?v=4) |


------


## `Licenças`

Esse projeto é licenciado pela [GPLv3](https://www.gnu.org/licenses/gpl-3.0.pt-br.html).
