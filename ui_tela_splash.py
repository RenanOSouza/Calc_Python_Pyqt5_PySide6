from PyQt5 import QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient,QMovie)
from PySide6.QtWidgets import *



class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(337, 300)
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
            "	background-color: rgb(255,255,255);\n"
            "	rgb: (170, 0, 255);\n"
            "	border-radius: 10px;\n"
            "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)

        self.label_movie = QLabel(self.dropShadowFrame)
        self.label_movie.setGeometry(QRect(0,0, 337,300))
        self.label_movie.setMinimumSize(QSize(337, 290))
        self.label_movie.setMaximumSize(QSize(337, 290))
        self.label_movie.setStyleSheet(u"color: rgb(255,0,0);border-radius: 10px;")
        self.movie = QMovie("teste.gif")
        self.label_movie.setMovie(self.movie)
        self.movie.start()

        self.label_titulo = QLabel(self.dropShadowFrame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(10,0, 200, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(26)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet(u"color: rgba(232, 49, 49, 255); background-color: transparent;")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_descricao = QLabel(self.dropShadowFrame)
        self.label_descricao.setObjectName(u"label_descricao")
        self.label_descricao.setGeometry(QRect(15, 60, 200, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_descricao.setFont(font1)
        self.label_descricao.setStyleSheet(u"color: rgb(255,255,255); background-color: transparent;")
        self.label_descricao.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 212, 295, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
            "	background-color: rgb(255,255, 255);\n"
            "	color: rgb(200, 200, 200);\n"
            "	border-style: none;\n"
            "	border-radius: 10px;\n"
            "	text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk{\n"
            "	border-radius: 10px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(240,91, 91, 255), stop: 1 rgba(232, 49, 49, 255));\n"
            "}")
        self.progressBar.setValue(24)
        self.label_carregando = QLabel(self.dropShadowFrame)
        self.label_carregando.setObjectName(u"label_carregando")
        self.label_carregando.setGeometry(QRect(0, 360, 300, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.label_carregando.setFont(font2)
        self.label_carregando.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_carregando.setAlignment(Qt.AlignCenter)

    
        self.verticalLayout.addWidget(self.dropShadowFrame)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Splash", u"Splash", None))
        self.label_titulo.setText(QCoreApplication.translate("Splash", u"<strong>RocketCalc</strong>", None))
        self.label_descricao.setText(QCoreApplication.translate("Splash", u" Descri\u00e7\u00e3o...", None))
        self.label_carregando.setText(QCoreApplication.translate("Splash", u"Carregando...", None))
    # retranslateUi

