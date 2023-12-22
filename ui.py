# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 895)
        MainWindow.setStyleSheet("background:rgb(52, 62, 39);\n"
"color:white;\n"
"font-size:20px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.folder_btn.setGeometry(QtCore.QRect(30, 710, 147, 32))
        self.folder_btn.setObjectName("folder_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(50, 750, 91, 32))
        self.save_btn.setObjectName("save_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(20, 30, 182, 32))
        self.right_btn.setObjectName("right_btn")
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(220, 30, 165, 32))
        self.left_btn.setObjectName("left_btn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 181, 581))
        self.listWidget.setObjectName("listWidget")
        self.blur_btn = QtWidgets.QPushButton(self.centralwidget)
        self.blur_btn.setGeometry(QtCore.QRect(410, 30, 92, 32))
        self.blur_btn.setObjectName("blur_btn")
        self.bw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bw_btn.setGeometry(QtCore.QRect(530, 30, 110, 32))
        self.bw_btn.setObjectName("bw_btn")
        self.mirror_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_btn.setGeometry(QtCore.QRect(650, 30, 130, 32))
        self.mirror_btn.setObjectName("mirror_btn")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(265, 131, 701, 581))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 34))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyEditor"))
        self.folder_btn.setText(_translate("MainWindow", "Відркити папку"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.right_btn.setText(_translate("MainWindow", "Повернути в право"))
        self.left_btn.setText(_translate("MainWindow", "Повернути в ліво"))
        self.blur_btn.setText(_translate("MainWindow", "Розмиття"))
        self.bw_btn.setText(_translate("MainWindow", "Чорно-біле"))
        self.mirror_btn.setText(_translate("MainWindow", "Відзеркалити"))
        self.menu.setTitle(_translate("MainWindow", "Редагувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
