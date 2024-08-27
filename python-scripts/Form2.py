from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import pyodbc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1600, 1600))
        self.label.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(1)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 301, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 200, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(600, 60, 450, 50))
        self.lineEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 120, 450, 50))
        self.lineEdit_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 200, 450, 51))
        self.lineEdit_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 300, 51))  # Adjusted width
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(194, 194, 210);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 280, 450, 300))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Dell/Downloads/genericphoto.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 600, 450, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.upload_photo)
        self.pushButton_2.clicked.connect(self.submit_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "First Name "))
        self.label_3.setText(_translate("MainWindow", "Last Name "))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.pushButton.setText(_translate("MainWindow", "Upload "))  # Adjusted button text
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))

    def upload_photo(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Image files (*.jpg *.png)")
        filename = file_dialog.getOpenFileName()[0]
        if filename:
            pixmap = QtGui.QPixmap(filename)
            self.label_5.setPixmap(pixmap)

    def reset_form(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Dell/Downloads/genericphoto.png"))


    def submit_data(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        server = 'DESKTOP-FKSHIM8\SQLEXPRESS01'
        database = 'Cybex'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        cursor = conn.cursor()

        query = "INSERT INTO form_2 (First_Name, Last_Name, Email) VALUES (?, ?, ?)"
        cursor.execute(query, (first_name, last_name, email))
        conn.commit()

        conn.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data sent successfully.")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.reset_form()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
