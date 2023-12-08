from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
import traceback
from datetime import datetime



class Ui_Dialog(object):
    def __init__(self, table_name):
        self.TABLE = table_name
        self.db = sqlite3.connect('Register.db')
        self.cursor = self.db.cursor()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 560)
        Dialog.setStyleSheet("background-color: rgba(109, 105, 105, 0.8);")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 710, 360))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("border: none; border-radius:7px")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 130, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 20, 130, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setGeometry(QtCore.QRect(600, 470, 145, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 470, 145, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 440, 400, 80))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText('Введите тест...')
        self.textEdit.setStyleSheet("""
        background-color: rgba(55, 40, 40, 0.15); 
        font-size: 15px;
        border: None; 
        border-radius: 5px;                                     
        """)

        btns = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4]
        for btn in btns:
            btn.setStyleSheet("""
            background-color: rgba(55, 40, 40, 0.2); 
            color: black;
            font-size: 14px; 
            border: None; 
            border-radius: 5px;}
            QPushButton:hover {
            background-color: rgba(55, 40, 40, 0.35);                                                           
                """)

        self.upload_data()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def upload_data(self):
        query = f"SELECT * FROM {self.TABLE}"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        column_names = [column[0] for column in self.cursor.description]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(column_names)
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Детальные сведения"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_3.setText(_translate("MainWindow", "Записать изменения"))
        self.pushButton_4.setText(_translate("MainWindow", "Отменить изменения"))
        self.pushButton.clicked.connect(self.delete_selected)
        self.pushButton_2.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.upload_changes)
        self.pushButton_4.clicked.connect(self.cancel_changes)

    def delete_selected(self):
        try:
            selected_rows = self.tableWidget.selectedItems()
            if not selected_rows:
                return
            selected_row_ids = set(item.row() for item in selected_rows)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Удалить строки')
            msg.setText("Вы уверены, что хотите удалить выбранные строку(ки)?")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            btn = msg.exec_()
            if btn == QtWidgets.QMessageBox.Ok:

                self.files_for_delete = selected_rows
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle('Удалить строки')
                msg.setText("Для подтверждения удаления нажмите кнопку Запись, для отмены изменений нажмите Отмена")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                btn2 = msg.exec_()

                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)

        except Exception as e:
            traceback.print_exc()

    def check_data_type(self, data, expected_type):
        if expected_type.lower() == 'integer':
            try:
                int(data)
                return True
            except ValueError:
                return False
        elif expected_type.lower() == 'real':
            try:
                float(data)
                return True
            except ValueError:
                return False
        elif expected_type.lower() == 'text' or expected_type.lower() == 'text(50)':
            if len(data) <= 50:
                return True
            else:
                False
        elif expected_type.lower() == 'datetime':
            formats = ['%d.%m.%Y %H:%M', '%d.%m.%Y']
            for format in formats:
                try:
                    datetime.strptime(data, format)
                    return True
                except ValueError:
                    return False
        else:
            return False

    def add_data(self):
        try:
            entered_text = self.textEdit.toPlainText()
            if not entered_text:
                return
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("После добавления и проверки данных, нажмите кнопку 'Записать', чтобы поместить данные в таблицу.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            btn = msg.exec_()
            if btn == QtWidgets.QMessageBox.Ok:
                entered_text_list = entered_text.split(',')

                column_data_types = self.cursor.execute(f"PRAGMA table_info({self.TABLE})").fetchall()

                for i, data in enumerate(entered_text_list, start=1):
                    data = data.strip()
                    if not self.check_data_type(data, column_data_types[i][2]):

                        error = ValueError(f"Некорректный ввод данных в поле {column_data_types[i][1]}, допустим тип данных только {column_data_types[i][2]}")
                        msg.setText(str(error))
                        msg.exec_()
                        return

                self.files_for_upload = entered_text_list
                self.textEdit.clear()

                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)

        except Exception as e:
            traceback.print_exc()

    files_for_delete = None
    files_for_upload = None
    def upload_changes(self):
        try:
            if self.files_for_upload is not None:
                query = f"INSERT INTO {self.TABLE} VALUES (NULL, {', '.join(['?'] * len(self.files_for_upload))})"
                self.cursor.execute(query, tuple(self.files_for_upload))

                self.db.commit()
                self.upload_data()

            if self.files_for_delete is not None:
                for item in self.files_for_delete:
                    row_id = item.row()
                    item = self.tableWidget.item(row_id, 0)
                    if item is not None:
                        item_id = int(item.text())
                        self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.TABLE), (item_id,))

                self.db.commit()
                self.upload_data()

        except Exception as e:
            traceback.print_exc()

        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)

    def cancel_changes(self):
        self.files_for_delete = None
        self.files_for_upload = None

        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

