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
   |-  📁 src
   |    |
   |    |- 📁 assets
   |         |- 📄 imagem.svg
   |
   |    |- 📁 components
   |         |- 📁 Banner 
   |                |- 📄 index.js
   |                |- 📄 styles.css
   |         |- 📁 Menu 
   |                |- 📄 index.js
   |                |- 📄 styles.css
   |
   |    |- 📁 routes
   |         |- 📄 Routes.js 
   |    
   |
   |
   |    |- 📄 App.js
   |    |- 📄 index.js
   |    |- 📄 global.css
   |

```
Descrição dos arquivos:
* `Arquivo:` Descrição
* `Arquivo:` Descrição
* `Arquivo:` Descrição


------


## `Dificuldades enfrentadas`

Ao decorrer da idealização e do desenvolvimento do projeto, algumas dificuldades foram enfrentadas, mas, a partir disso, algumas lições foram aprendidas, conforme os tópicos a seguir:

* `Maior erro enfrentado e como lidamos com ele:` Estabelecemos muitas features para o projeto, mas não priorizamos e nem levamos em consideração os requisitos básicos propostos pelos orientadores. Nesse contexto, com um pouco menos de tempo para o desenvolvimento, percebemos isso e nos reunimos para mudar o escopo, cumprindo primordialmente os requistos básicos e deixando outras features em stand by. Dessa forma, foi possível garantir o básico e, somente assim, partir para o mais complexo.
* `Maior desafio enfrentado e como lidamos com ele:`
* `Lições aprendidas durante o projeto:`


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

Colocar aqui as linceças do projeto
