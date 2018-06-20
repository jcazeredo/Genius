from Interface import Interface
from Mediador import Mediador
from ControleJogo import ControleJogo
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Genius = QtWidgets.QMainWindow()

    mediador = Mediador()
    interface = Interface(Genius, mediador)
    controle = ControleJogo(mediador)
    mediador.definirControle(controle)
    mediador.definirInterface(interface)


    Genius.show()
    sys.exit(app.exec_())
