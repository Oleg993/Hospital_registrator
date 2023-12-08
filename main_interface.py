from PyQt5 import QtCore, QtGui, QtWidgets
from dialog_table import Ui_Dialog
from functools import partial
import sqlite3


db = sqlite3.connect('Register.db')
cursor = db.cursor()

# a = """
# self.centralwidget = QtWidgets.QWidget(MainWindow)
# self.centralwidget.setObjectName("MainWindow")
# self.centralwidget.setStyleSheet("QPushButton { background-color: red; color: white; }")
# self.pushButton = QtWidgets.QPushButton(self.centralwidget)
# self.pushButton.setGeometry(QtCore.QRect(40, 180, 130, 80))
# self.pushButton.setObjectName("pushButton")
# self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
# self.pushButton_2.setGeometry(QtCore.QRect(230, 180, 130, 80))
# self.pushButton_2.setObjectName("pushButton_2")
# self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
# self.pushButton_3.setGeometry(QtCore.QRect(420, 180, 130, 80))
# self.pushButton_3.setObjectName("pushButton_3")
# self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
# self.pushButton_4.setGeometry(QtCore.QRect(610, 180, 130, 80))
# self.pushButton_4.setObjectName("pushButton_4")
# self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
# self.pushButton_5.setGeometry(QtCore.QRect(320, 330, 130, 80))
# self.pushButton_5.setObjectName("pushButton_5")
# """
# dicty = {"1": a}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: gray;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("MainWindow")
        self.centralwidget.setStyleSheet(""" QPushButton { 
                                        background-color: rgba(109, 105, 105, 0.7); 
                                        color: black;
                                        font-size: 17px; 
                                        border: None; 
                                        border-radius: 7px;}
                                        QPushButton:hover {
                                        background-color: rgba(109, 105, 105, 0.5);
                                        font-size: 18px; 
                                        }""")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 145, 95))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 180, 145, 95))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 180, 145, 95))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 180, 145, 95))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 330, 145, 95))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистратура"))
        self.pushButton.setText(_translate("MainWindow", "Клиенты"))
        self.pushButton_2.setText(_translate("MainWindow", "Врачи"))
        self.pushButton_3.setText(_translate("MainWindow", "Должности"))
        self.pushButton_4.setText(_translate("MainWindow", "Услуги"))
        self.pushButton_5.setText(_translate("MainWindow", "Запись"))
        self.pushButton.clicked.connect(partial(self.table_dialog, 'Клиенты'))
        self.pushButton_2.clicked.connect(partial(self.table_dialog, 'Сотрудники'))
        self.pushButton_3.clicked.connect(partial(self.table_dialog, 'Должности'))
        self.pushButton_4.clicked.connect(partial(self.table_dialog, 'Услуги'))
        self.pushButton_5.clicked.connect(partial(self.table_dialog, '[Оказанные услуги]'))

    def table_dialog(self, table_name):
        Dialog = QtWidgets.QDialog()
        ui_table = Ui_Dialog(table_name)
        ui_table.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
