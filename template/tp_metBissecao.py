# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_metBissecao.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MetBissecao(object):
    def setupUi(self, MetBissecao):
        MetBissecao.setObjectName("MetBissecao")
        MetBissecao.resize(783, 637)
        MetBissecao.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(MetBissecao)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.but_calc = QtWidgets.QPushButton(self.centralwidget)
        self.but_calc.setGeometry(QtCore.QRect(420, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_calc.setFont(font)
        self.but_calc.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_calc.setObjectName("but_calc")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(240, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_clear.setFont(font)
        self.but_clear.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_clear.setObjectName("but_clear")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 290, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(30, 510, 741, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 38, 38);")
        self.labelResult.setText("")
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 320, 751, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 220, 18, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_valA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_valA.setGeometry(QtCore.QRect(204, 220, 167, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_valA.setFont(font)
        self.lineEdit_valA.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_valA.setObjectName("lineEdit_valA")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(398, 220, 18, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_valA_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_valA_2.setGeometry(QtCore.QRect(422, 220, 167, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_valA_2.setFont(font)
        self.lineEdit_valA_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_valA_2.setObjectName("lineEdit_valA_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 180, 191, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.inp_expr_Biss = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_expr_Biss.setGeometry(QtCore.QRect(120, 93, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inp_expr_Biss.setFont(font)
        self.inp_expr_Biss.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_expr_Biss.setInputMask("")
        self.inp_expr_Biss.setText("")
        self.inp_expr_Biss.setObjectName("inp_expr_Biss")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(31, 99, 65, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.inp_tolBiss = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_tolBiss.setGeometry(QtCore.QRect(120, 146, 167, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inp_tolBiss.setFont(font)
        self.inp_tolBiss.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_tolBiss.setText("")
        self.inp_tolBiss.setObjectName("inp_tolBiss")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 150, 79, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 180, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 580, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lblTempExib = QtWidgets.QLabel(self.centralwidget)
        self.lblTempExib.setGeometry(QtCore.QRect(680, 580, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTempExib.setFont(font)
        self.lblTempExib.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTempExib.setText("")
        self.lblTempExib.setObjectName("lblTempExib")
        MetBissecao.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MetBissecao)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        MetBissecao.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MetBissecao)
        self.statusbar.setObjectName("statusbar")
        MetBissecao.setStatusBar(self.statusbar)

        self.retranslateUi(MetBissecao)
        QtCore.QMetaObject.connectSlotsByName(MetBissecao)

    def retranslateUi(self, MetBissecao):
        _translate = QtCore.QCoreApplication.translate
        MetBissecao.setWindowTitle(_translate("MetBissecao", "Método Bisseção"))
        self.label.setText(_translate("MetBissecao", "Método Bisseção"))
        self.but_calc.setText(_translate("MetBissecao", "Calcular"))
        self.but_clear.setText(_translate("MetBissecao", "Limpar"))
        self.label_6.setText(_translate("MetBissecao", "Resultado:"))
        self.label_2.setText(_translate("MetBissecao", "A:"))
        self.label_4.setText(_translate("MetBissecao", "B:"))
        self.radioButton.setText(_translate("MetBissecao", "valor de A e B manual:"))
        self.inp_expr_Biss.setPlaceholderText(_translate("MetBissecao", "Ex.: 2*x**2 + x + 1 | x + log10(x)"))
        self.label_8.setText(_translate("MetBissecao", "Equação:"))
        self.inp_tolBiss.setPlaceholderText(_translate("MetBissecao", "Ex.: 0.001 | 10**-3"))
        self.label_3.setText(_translate("MetBissecao", "Tolerancia:"))
        self.radioButton_2.setText(_translate("MetBissecao", "valor de A e B automatico:"))
        self.label_7.setText(_translate("MetBissecao", "Execução:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MetBissecao = QtWidgets.QMainWindow()
    ui = Ui_MetBissecao()
    ui.setupUi(MetBissecao)
    MetBissecao.show()
    sys.exit(app.exec_())
