# Genius Game


### Requisitos
- Miniconda (versão mini do Anaconda)
- Python 3.5/3.6
- Pacotes Python:
    - PyQT5
    - PyGame

### Instalação (WINDOWS)
***1)*** Baixe aqui o [Miniconda](https://conda.io/miniconda.html). 

***2)*** Ao instalar, guarde o local de instalação e MARQUE as caixas de seleção `Add Anaconda to my PATH environment variable` e `Register Anaconda as my default Python 3.6`

***3)*** Teste se ocorreu tudo certo, abrindo o prompt de comando e digitando:
```sh
$ conda --version
```
Caso o resultado seja a versão do programa instalado , então a instalação deu certo.

***4)*** Crie um ambiente novo
```sh
$ conda create -n genius python=3.6
```
Caso prompt peça para confirmar a instalação, digite SIM/YES

***5)*** Instale os seguintes pacotes
```sh
$ conda install pyqt
$ conda -c cogsci pygame
```
Caso o terminal peça para confirmar a instalação, digite SIM/YES

***6)*** Ative o ambiente criado
```sh
$ activate genius
```
Repare que o terminal deve ficar da seguinte forma:
```sh
(genius) $
```

***7)*** Entre na pasta onde está localizado o arquivo genius.py e execute o comando abaixo:
```sh
(genius) $ python genius.py
```

Nesse momento, o programa deve abrir normalmente e você poderá iniciar o jogo.

