# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from threading import Thread
from threading import Timer
from FaceSearcher import searchFaceFromFolder
import time
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 548)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(290, 420, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(240, 130, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textEdit.setFont(font)

        self.textEdit.setObjectName("textEdit")


        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 170, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.btn_img_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_img_browse.setGeometry(QtCore.QRect(580, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_img_browse.setFont(font)
        self.btn_img_browse.setObjectName("pushButton_2")
        self.btn_img_browse.clicked.connect(self.openFileNameDialog)

        self.btn_folder_to_search_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_folder_to_search_browse.setGeometry(QtCore.QRect(580, 170, 75, 23))

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_folder_to_search_browse.setFont(font)
        self.btn_folder_to_search_browse.setObjectName("pushButton_3")
        self.btn_folder_to_search_browse.clicked.connect(self.openFolderDialog)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 210, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText("results")
        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setGeometry(QtCore.QRect(70, 340, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.label_progress.setFont(font)
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)

        self.label_progress.setObjectName("label_progress")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setEnabled(True)
        self.label_error.setGeometry(QtCore.QRect(60, 270, 660, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.label_error.setFont(font)
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #     Vraiables
        self.input_img_path=""
        self.folder_to_search=""
        self.destination_folder=""



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Face Image"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_start.clicked.connect(self.test)
        self.label_2.setText(_translate("MainWindow", "Select Folder to Search"))
        self.btn_img_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_folder_to_search_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Output Folder Name"))
        self.textEdit_3.setText("results")
#         self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_progress.setText(_translate("MainWindow", "Progress : 0%"))



    def startSearch(self):
        start = time.time()

        try:
            os.mkdir(self.destination_folder)
        except:
            pass
        try:
            total,copied=searchFaceFromFolder(self.input_img_path, self.folder_to_search, self.destination_folder,self.label_progress)
            if(total==None):
                self.label_error.setText("Multiple Faces in input image")
            else:
                self.label_error.setText(str(copied)+" images copied to "+ self.destination_folder)
        except:
            self.label_error.setText("Error")
        end = time.time()
        print("Time taken", end - start)

    def test(self):
        flag=True;
        self.input_img_path=self.textEdit.toPlainText()

        flag=flag and os.path.exists(self.input_img_path)
        self.folder_to_search=self.textEdit_2.toPlainText()

        flag = flag and os.path.exists(self.folder_to_search)

        self.destination_folder=self.textEdit_3.toPlainText()

        if(flag==False):
            self.label_error.setText("Error :Kindly give proper path")
        else:
            self.label_error.setText("Processing . . .")
            self.label_progress.setText("Progress : 0%")
            # self.startSearch(input_img_path,folder_to_search,destination_folder)
            t=Thread(target=self.startSearch)
            t.start()



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*.jpg);;Image Files (*.PNG)", options=options)
        if fileName:

            print(fileName)
            self.textEdit.setText(fileName)

    def openFolderDialog(self):
        folder_path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        print(folder_path)
        self.textEdit_2.setText(folder_path)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


