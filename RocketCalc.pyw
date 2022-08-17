import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QGuiApplication, QMovie, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore,  QtWidgets
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *
from tkinter.filedialog import askopenfilename
from tkinter import *
from ui_tela_splash import Ui_Splash
from ui_tela_push import Ui_ViewPush
from ui_main_screen import Ui_MainWindow
import time


## definindo global
counter = 0

# Tela Login
class MainWindow(QMainWindow):
    
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.visor = ""

        ## Limpeza na tela
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ## Efeito de Sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        
        #Ação dos Botões Iniciais
        self.ui.btn_deslogar.clicked.connect(lambda: sys.exit())
        self.ui.btn_0.clicked.connect(lambda: self.apresentar("0"))
        self.ui.btn_1.clicked.connect(lambda: self.apresentar("1"))
        self.ui.btn_2.clicked.connect(lambda: self.apresentar("2"))
        self.ui.btn_3.clicked.connect(lambda: self.apresentar("3"))
        self.ui.btn_4.clicked.connect(lambda: self.apresentar("4"))
        self.ui.btn_5.clicked.connect(lambda: self.apresentar("5"))
        self.ui.btn_6.clicked.connect(lambda: self.apresentar("6"))
        self.ui.btn_7.clicked.connect(lambda: self.apresentar("7"))
        self.ui.btn_8.clicked.connect(lambda: self.apresentar("8"))
        self.ui.btn_9.clicked.connect(lambda: self.apresentar("9"))
        self.ui.btn_c.clicked.connect(self.apagarTudo)
        self.ui.btn_adicao.clicked.connect(lambda: self.apresentar("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.apresentar("-"))
        self.ui.btn_apagar.clicked.connect(self.apagar)
        self.ui.btn_mult.clicked.connect(lambda: self.apresentar("*"))
        self.ui.btn_porcentagem.clicked.connect(lambda: self.apresentar("."))
        self.ui.btn_divisao.clicked.connect(lambda: self.apresentar("/"))
        self.ui.btn_igual.clicked.connect(self.processar)

    def apagarTudo(self):
        self.visor = " 0"
        self.ui.campo_total.setText(self.visor)

    def apresentar(self,valor):
        self.visor += valor
        self.ui.campo_total.setText(self.visor)
    
    def apagar(self):
        self.visor = self.visor[:len(self.visor)-1]
        self.ui.campo_total.setText(self.visor)

    def processar(self):
        result = str(eval(self.visor))
        self.ui.campo_total.setText(result)
        self.visor = " "
        
# Tela Splash
class Splash(QMainWindow):
    app = QGuiApplication(sys.argv)

    def __init__(self):
        super(Splash, self).__init__()
        #QMainWindow.__init__(self)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        ## Limpeza na tela
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## Efeito de Sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## Definição de tempo da tela de carregamento
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        
        # Tempo definido em ms
        self.timer.start(50)

        ## Mudança de texto da descrição
        # Definição de texto inicial
        self.ui.label_descricao.setText("<strong>Bem</strong> Vindo ao APP")

        # Mudança nos textos de carregamento
        QtCore.QTimer.singleShot(2500, lambda: self.ui.label_descricao.setText("<strong>Carregando</strong> o sistema..."))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.label_descricao.setText("<strong>Carregando</strong> Tela Inicial..."))
        ## Chama a tela
        self.show()
    
    
    ## Funções do Aplicativo
    def progress(self):

        global counter

        # Definição de valor da barra de progresso
        self.ui.progressBar.setValue(counter)

        # Definição de tempo para fechar a tela de Splash e abrir a tela de login
        if counter > 100:
            # Para o tempo
            self.timer.stop()

            # Chama a tela de Login
            self.main = MainWindow()
            self.main.show()

            # Fecha a tela de Spash
            self.close()

        # Contador
        counter += 1

# Inicialização
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Splash()
    sys.exit(app.exec())


