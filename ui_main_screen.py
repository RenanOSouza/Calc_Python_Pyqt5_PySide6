from sys import set_asyncgen_hooks
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                if not MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                        MainWindow.resize(300, 415)
                        self.centralwidget = QWidget(MainWindow)
                        self.centralwidget.setObjectName(u"centralwidget")
                        self.verticalLayout = QVBoxLayout(self.centralwidget)
                        self.verticalLayout.setObjectName(u"verticalLayout")
                        self.dropShadowFrame = QFrame(self.centralwidget)
                        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
                        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
                                "	background-color: rgb(85, 85, 85);\n"
                                "	rgb: (170, 0, 255);\n"
                                "	border-radius: 10px;\n"
                                "}")
                        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
                        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
                        self.label_tituloLogin = QLabel(self.dropShadowFrame)
                        self.label_tituloLogin.setObjectName(u"label_tituloLogin")
                        self.label_tituloLogin.setGeometry(QRect(25,0, 230, 40))
                        font = QFont()
                        font.setFamily(u"Segoe UI")
                        font.setPointSize(20)
                        self.label_tituloLogin.setFont(font)
                        self.label_tituloLogin.setStyleSheet(u"color: rgba(232, 49, 49, 255);")
                        self.label_tituloLogin.setAlignment(Qt.AlignCenter)

                        self.label_tituloRocket = QLabel(self.dropShadowFrame)
                        self.label_tituloRocket.setObjectName(u"label_tituloRocket")
                        self.label_tituloRocket.setGeometry(QRect(25,35, 230, 40))
                        font = QFont()
                        font.setFamily(u"Segoe UI")
                        font.setPointSize(20)
                        self.label_tituloRocket.setFont(font)
                        self.label_tituloRocket.setStyleSheet(u"color: rgba(232, 49, 49, 255);")
                        self.label_tituloRocket.setAlignment(Qt.AlignCenter)

                        self.campo_total = QLineEdit(self.dropShadowFrame)
                        self.campo_total.setObjectName(u"campo_total")
                        self.campo_total.setGeometry(QRect(5, 100, 270, 41))
                        font2 = QFont()
                        font2.setFamily(u"Segoe UI")
                        font2.setPointSize(12)
                        font2.setBold(False)
                        #font2.setWeight(50)
                        self.campo_total.setFont(font2)
                        self.campo_total.setCursor(QCursor(Qt.WaitCursor))
                        self.campo_total.setStyleSheet(u"background-color: rgb(187, 187, 186);\n"
                                "border:none;\n"
                                "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                "color: rgba(255, 255, 255, 210);\n"
                                "padding-bottom:7px;\n"
                                "text-align: center;\n"
                                "\n"
                                "")
                        self.campo_total.setAlignment(Qt.AlignCenter)
                        self.campo_total.setDisabled(True)                   
                        self.btn_deslogar = QPushButton(self.dropShadowFrame)
                        self.btn_deslogar.setObjectName(u"btn_deslogar")
                        self.btn_deslogar.setGeometry(QRect(238, 3, 41, 31))
                        font4 = QFont()
                        font4.setFamily(u"Segoe UI")
                        font4.setPointSize(10)
                        font4.setBold(True)
                        font4.setItalic(False)
                        #font4.setWeight(75)
                        self.btn_deslogar.setFont(font4)
                        self.btn_deslogar.setStyleSheet(u"QPushButton#btn_deslogar{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_deslogar:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_deslogar:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        
                        self.btn_c = QPushButton(self.dropShadowFrame)
                        self.btn_c.setObjectName(u"btn_c")
                        self.btn_c.setGeometry(QRect(5,150, 62, 41))
                        self.btn_c.setFont(font4)
                        self.btn_c.setStyleSheet(u"QPushButton#btn_c{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_c:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_c:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_apagar = QPushButton(self.dropShadowFrame)
                        self.btn_apagar.setObjectName(u"btn_apagar")
                        self.btn_apagar.setGeometry(QRect(75,150, 61, 41))
                        self.btn_apagar.setFont(font4)
                        self.btn_apagar.setStyleSheet(u"QPushButton#btn_apagar{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_apagar:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_apagar:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_porcentagem = QPushButton(self.dropShadowFrame)
                        self.btn_porcentagem.setObjectName(u"btn_porcentagem")
                        self.btn_porcentagem.setGeometry(QRect(145, 150, 61, 41))
                        self.btn_porcentagem.setFont(font4)
                        self.btn_porcentagem.setStyleSheet(u"QPushButton#btn_porcentagem{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_porcentagem:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_porcentagem:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_divisao = QPushButton(self.dropShadowFrame)
                        self.btn_divisao.setObjectName(u"btn_divisao")
                        self.btn_divisao.setGeometry(QRect(215, 150, 61, 41))
                        self.btn_divisao.setFont(font4)
                        self.btn_divisao.setStyleSheet(u"QPushButton#btn_divisao{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_divisao:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_divisao:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")

                        self.btn_7 = QPushButton(self.dropShadowFrame)
                        self.btn_7.setObjectName(u"btn_7")
                        self.btn_7.setGeometry(QRect(5,200, 62, 41))
                        self.btn_7.setFont(font4)
                        self.btn_7.setStyleSheet(u"QPushButton#btn_7{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_7:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_7:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_8 = QPushButton(self.dropShadowFrame)
                        self.btn_8.setObjectName(u"btn_8")
                        self.btn_8.setGeometry(QRect(75,200, 61, 41))
                        self.btn_8.setFont(font4)
                        self.btn_8.setStyleSheet(u"QPushButton#btn_8{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_8:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_8:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_9 = QPushButton(self.dropShadowFrame)
                        self.btn_9.setObjectName(u"btn_9")
                        self.btn_9.setGeometry(QRect(145, 200, 61, 41))
                        self.btn_9.setFont(font4)
                        self.btn_9.setStyleSheet(u"QPushButton#btn_9{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_9:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_9:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_mult = QPushButton(self.dropShadowFrame)
                        self.btn_mult.setObjectName(u"btn_mult")
                        self.btn_mult.setGeometry(QRect(215, 200, 61, 41))
                        self.btn_mult.setFont(font4)
                        self.btn_mult.setStyleSheet(u"QPushButton#btn_mult{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_mult:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_mult:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")

                        
                        self.btn_4 = QPushButton(self.dropShadowFrame)
                        self.btn_4.setObjectName(u"btn_4")
                        self.btn_4.setGeometry(QRect(5,250, 62, 41))
                        self.btn_4.setFont(font4)
                        self.btn_4.setStyleSheet(u"QPushButton#btn_4{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_4:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_4:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_5 = QPushButton(self.dropShadowFrame)
                        self.btn_5.setObjectName(u"btn_5")
                        self.btn_5.setGeometry(QRect(75,250, 61, 41))
                        self.btn_5.setFont(font4)
                        self.btn_5.setStyleSheet(u"QPushButton#btn_5{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_5:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_5:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_6 = QPushButton(self.dropShadowFrame)
                        self.btn_6.setObjectName(u"btn_6")
                        self.btn_6.setGeometry(QRect(145, 250, 61, 41))
                        self.btn_6.setFont(font4)
                        self.btn_6.setStyleSheet(u"QPushButton#btn_6{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_6:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_6:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_sub = QPushButton(self.dropShadowFrame)
                        self.btn_sub.setObjectName(u"btn_sub")
                        self.btn_sub.setGeometry(QRect(215, 250, 61, 41))
                        self.btn_sub.setFont(font4)
                        self.btn_sub.setStyleSheet(u"QPushButton#btn_sub{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_sub:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_sub:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        
                        self.btn_1 = QPushButton(self.dropShadowFrame)
                        self.btn_1.setObjectName(u"btn_1")
                        self.btn_1.setGeometry(QRect(5,300, 62, 41))
                        self.btn_1.setFont(font4)
                        self.btn_1.setStyleSheet(u"QPushButton#btn_1{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_1:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_1:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_2 = QPushButton(self.dropShadowFrame)
                        self.btn_2.setObjectName(u"btn_2")
                        self.btn_2.setGeometry(QRect(75,300, 61, 41))
                        self.btn_2.setFont(font4)
                        self.btn_2.setStyleSheet(u"QPushButton#btn_2{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_2:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_2:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_3 = QPushButton(self.dropShadowFrame)
                        self.btn_3.setObjectName(u"btn_3")
                        self.btn_3.setGeometry(QRect(145, 300, 61, 41))
                        self.btn_3.setFont(font4)
                        self.btn_3.setStyleSheet(u"QPushButton#btn_3{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_3:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_3:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        self.btn_adicao = QPushButton(self.dropShadowFrame)
                        self.btn_adicao.setObjectName(u"btn_adicao")
                        self.btn_adicao.setGeometry(QRect(215, 300, 61, 41))
                        self.btn_adicao.setFont(font4)
                        self.btn_adicao.setStyleSheet(u"QPushButton#btn_adicao{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_adicao:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_adicao:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        
                        self.btn_0 = QPushButton(self.dropShadowFrame)
                        self.btn_0.setObjectName(u"btn_0")
                        self.btn_0.setGeometry(QRect(5,350, 130, 41))
                        self.btn_0.setFont(font4)
                        self.btn_0.setStyleSheet(u"QPushButton#btn_0{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_0:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_0:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")
                        
                        self.btn_igual = QPushButton(self.dropShadowFrame)
                        self.btn_igual.setObjectName(u"btn_igual")
                        self.btn_igual.setGeometry(QRect(145, 350, 130, 41))
                        self.btn_igual.setFont(font4)
                        self.btn_igual.setStyleSheet(u"QPushButton#btn_igual{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(226, 1, 12, 0.4), stop: 1 rgba(255, 34, 43, 0.8));\n"
                                "	color: rgba(255, 255, 255, 210);\n"
                                "	border-radius: 10px;\n"
                                "}\n"
                                "QPushButton#btn_igual:hover{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:1 rgba(255, 34, 43, 0.4), stop:0 rgba(226, 1, 12, 0.5));\n"
                                "}\n"
                                "QPushButton#btn_igual:pressed{\n"
                                "	background-color: rgba(255, 34, 43, 0.8);\n"
                                "}")

                self.verticalLayout.addWidget(self.dropShadowFrame)

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)

                QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
                self.label_tituloLogin.setText(QCoreApplication.translate("MainWindow", u"<strong>Bem</strong>-vindo(a)", None))
                self.label_tituloRocket.setText(QCoreApplication.translate("MainWindow", u"<strong>RocketCalc</strong>", None))
                self.campo_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
                self.btn_deslogar.setText(QCoreApplication.translate("MainWindow", u"X", None))
                self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
                self.btn_apagar.setText(QCoreApplication.translate("MainWindow", u"<--", None))
                self.btn_porcentagem.setText(QCoreApplication.translate("MainWindow", u".", None))
                self.btn_divisao.setText(QCoreApplication.translate("MainWindow", u"÷", None))
                self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
                self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
                self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
                self.btn_mult.setText(QCoreApplication.translate("MainWindow", u"X", None))
                self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
                self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
                self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
                self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
                self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
                self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
                self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
                self.btn_adicao.setText(QCoreApplication.translate("MainWindow", u"+", None))
                self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
                self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))

        # retranslateUi

