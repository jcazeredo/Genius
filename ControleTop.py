import operator

class ControleTop:
    def __init__(self):
        self.__nomeArquivo = "src/ranking/top10.txt"
        self.__top10 = {}
        self.__menorPontuacao = 0

    def abrirArquivo(self):
        arquivo = open(self.__nomeArquivo, "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            split = linha.split(';')
            nome = split[0]
            pontos = split[1]
            self.__top10[nome] = int(pontos)
        self.__menorPontuacao = int(linha.split(";")[1])  #Atualiza a menor pontuação
        arquivo.close()

    def __salvarArquivo(self):
        arquivo = open(self.__nomeArquivo, "w")
        texto = []
        for i in range(10):
            jogador = self.__top10[i]
            texto.append(str(jogador[0]) + ';' + str(jogador[1]) + '\n')
        arquivo.writelines(texto)
        arquivo.close()


    def ordenarTop10(self):
        top10_Ordenado = sorted(self.__top10.items(), key=operator.itemgetter(1), reverse=True)
        self.__top10 = top10_Ordenado

    def estaNoTop10(self, pontuacao):
        self.abrirArquivo()
        if pontuacao >= self.__menorPontuacao:
            return True
        else:
            return False

    def addTop10(self, nome, pontuacao):
        self.__top10.update({nome:pontuacao})
        self.ordenarTop10()
        self.__salvarArquivo()

    def limparTop10(self):
        arquivo = open(self.__nomeArquivo, "w")
        texto = []
        for i in range(10):
            texto.append('Vazio'+ str(i+1) + ';' + '0' + '\n')
        arquivo.writelines(texto)
        arquivo.close()

    @property
    def getTop10(self):
        return self.__top10