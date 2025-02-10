# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 451))
        self.widget.setStyleSheet(u"background-color: rgb(202, 202, 202)")
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 30, 471, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tele_label = QLabel(self.gridLayoutWidget)
        self.tele_label.setObjectName(u"tele_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tele_label.setFont(font)

        self.gridLayout.addWidget(self.tele_label, 6, 0, 1, 1)

        self.id_label = QLabel(self.gridLayoutWidget)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font)

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.np_entry = QLineEdit(self.gridLayoutWidget)
        self.np_entry.setObjectName(u"np_entry")

        self.gridLayout.addWidget(self.np_entry, 1, 1, 1, 1)

        self.np_label = QLabel(self.gridLayoutWidget)
        self.np_label.setObjectName(u"np_label")
        self.np_label.setFont(font)

        self.gridLayout.addWidget(self.np_label, 1, 0, 1, 1)

        self.pv_label = QLabel(self.gridLayoutWidget)
        self.pv_label.setObjectName(u"pv_label")
        self.pv_label.setFont(font)

        self.gridLayout.addWidget(self.pv_label, 4, 0, 1, 1)

        self.est_entry = QLineEdit(self.gridLayoutWidget)
        self.est_entry.setObjectName(u"est_entry")

        self.gridLayout.addWidget(self.est_entry, 2, 1, 1, 1)

        self.nf_label = QLabel(self.gridLayoutWidget)
        self.nf_label.setObjectName(u"nf_label")
        self.nf_label.setFont(font)

        self.gridLayout.addWidget(self.nf_label, 5, 0, 1, 1)

        self.pc_label = QLabel(self.gridLayoutWidget)
        self.pc_label.setObjectName(u"pc_label")
        self.pc_label.setFont(font)

        self.gridLayout.addWidget(self.pc_label, 3, 0, 1, 1)

        self.pc_entry = QLineEdit(self.gridLayoutWidget)
        self.pc_entry.setObjectName(u"pc_entry")

        self.gridLayout.addWidget(self.pc_entry, 3, 1, 1, 1)

        self.est_label = QLabel(self.gridLayoutWidget)
        self.est_label.setObjectName(u"est_label")
        self.est_label.setFont(font)

        self.gridLayout.addWidget(self.est_label, 2, 0, 1, 1)

        self.id_entry = QLineEdit(self.gridLayoutWidget)
        self.id_entry.setObjectName(u"id_entry")
        self.id_entry.setStyleSheet(u"")

        self.gridLayout.addWidget(self.id_entry, 0, 1, 1, 1)

        self.pv_entry = QLineEdit(self.gridLayoutWidget)
        self.pv_entry.setObjectName(u"pv_entry")

        self.gridLayout.addWidget(self.pv_entry, 4, 1, 1, 1)

        self.nf_entry = QLineEdit(self.gridLayoutWidget)
        self.nf_entry.setObjectName(u"nf_entry")

        self.gridLayout.addWidget(self.nf_entry, 5, 1, 1, 1)

        self.tele_entry = QLineEdit(self.gridLayoutWidget)
        self.tele_entry.setObjectName(u"tele_entry")

        self.gridLayout.addWidget(self.tele_entry, 6, 1, 1, 1)

        self.cadstrar_btn = QPushButton(self.widget)
        self.cadstrar_btn.setObjectName(u"cadstrar_btn")
        self.cadstrar_btn.setGeometry(QRect(190, 390, 91, 31))
        self.Limpar_btn = QPushButton(self.widget)
        self.Limpar_btn.setObjectName(u"Limpar_btn")
        self.Limpar_btn.setGeometry(QRect(380, 390, 91, 31))
        self.Limpar_btn.setAutoFillBackground(False)
        self.Limpar_btn.setStyleSheet(u"background-color: rgb(255, 15, 19)")
        self.output = QTextEdit(self.widget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(560, 210, 104, 71))
        self.button = QPushButton(self.widget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(610, 320, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tele_label.setText(QCoreApplication.translate("MainWindow", u"Telefone do Fornecedor:", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.np_label.setText(QCoreApplication.translate("MainWindow", u"Nome do Produto: ", None))
        self.pv_label.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de Venda:", None))
        self.nf_label.setText(QCoreApplication.translate("MainWindow", u"Nome do Fornecedor:", None))
        self.pc_label.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de Custo:", None))
        self.est_label.setText(QCoreApplication.translate("MainWindow", u"Estoque:", None))
        self.cadstrar_btn.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.Limpar_btn.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

