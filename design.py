# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.categoriesWidget = QtWidgets.QWidget(self.centralwidget)
        self.categoriesWidget.setEnabled(True)
        self.categoriesWidget.setGeometry(QtCore.QRect(0, 0, 581, 541))
        self.categoriesWidget.setObjectName("categoriesWidget")
        self.categoriesTableWidget = QtWidgets.QTableWidget(self.categoriesWidget)
        self.categoriesTableWidget.setGeometry(QtCore.QRect(10, 30, 561, 361))
        self.categoriesTableWidget.setObjectName("categoriesTableWidget")
        self.categoriesTableWidget.setColumnCount(0)
        self.categoriesTableWidget.setRowCount(0)
        self.categoriesDeleteButton = QtWidgets.QPushButton(self.categoriesWidget)
        self.categoriesDeleteButton.setGeometry(QtCore.QRect(390, 400, 181, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categoriesDeleteButton.setIcon(icon)
        self.categoriesDeleteButton.setObjectName("categoriesDeleteButton")
        self.label = QtWidgets.QLabel(self.categoriesWidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.createCategoryLineEdit = QtWidgets.QLineEdit(self.categoriesWidget)
        self.createCategoryLineEdit.setGeometry(QtCore.QRect(120, 500, 271, 20))
        self.createCategoryLineEdit.setObjectName("createCategoryLineEdit")
        self.createCategoryButton = QtWidgets.QPushButton(self.categoriesWidget)
        self.createCategoryButton.setGeometry(QtCore.QRect(400, 500, 131, 23))
        self.createCategoryButton.setObjectName("createCategoryButton")
        self.label_2 = QtWidgets.QLabel(self.categoriesWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 500, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.categoriesWidget)
        self.label_3.setGeometry(QtCore.QRect(170, 470, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.saveCategoriesButton = QtWidgets.QPushButton(self.categoriesWidget)
        self.saveCategoriesButton.setGeometry(QtCore.QRect(10, 400, 191, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveCategoriesButton.setIcon(icon1)
        self.saveCategoriesButton.setObjectName("saveCategoriesButton")
        self.tasksWidget = QtWidgets.QWidget(self.centralwidget)
        self.tasksWidget.setGeometry(QtCore.QRect(10, 9, 561, 551))
        self.tasksWidget.setObjectName("tasksWidget")
        self.label_4 = QtWidgets.QLabel(self.tasksWidget)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.taskTableWidget = QtWidgets.QTableWidget(self.tasksWidget)
        self.taskTableWidget.setGeometry(QtCore.QRect(0, 40, 561, 201))
        self.taskTableWidget.setObjectName("taskTableWidget")
        self.taskTableWidget.setColumnCount(0)
        self.taskTableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.tasksWidget)
        self.label_5.setGeometry(QtCore.QRect(170, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.taskNameEdit = QtWidgets.QLineEdit(self.tasksWidget)
        self.taskNameEdit.setGeometry(QtCore.QRect(110, 360, 311, 20))
        self.taskNameEdit.setObjectName("taskNameEdit")
        self.label_6 = QtWidgets.QLabel(self.tasksWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tasksWidget)
        self.label_7.setGeometry(QtCore.QRect(40, 390, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tasksWidget)
        self.label_8.setGeometry(QtCore.QRect(10, 470, 101, 16))
        self.label_8.setObjectName("label_8")
        self.taskDateTimeEdit = QtWidgets.QDateTimeEdit(self.tasksWidget)
        self.taskDateTimeEdit.setGeometry(QtCore.QRect(110, 470, 111, 22))
        self.taskDateTimeEdit.setObjectName("taskDateTimeEdit")
        self.taskDescriptionEdit = QtWidgets.QTextEdit(self.tasksWidget)
        self.taskDescriptionEdit.setGeometry(QtCore.QRect(110, 390, 311, 71))
        self.taskDescriptionEdit.setObjectName("taskDescriptionEdit")
        self.selectCategoryComboBox = QtWidgets.QComboBox(self.tasksWidget)
        self.selectCategoryComboBox.setGeometry(QtCore.QRect(110, 330, 311, 22))
        self.selectCategoryComboBox.setObjectName("selectCategoryComboBox")
        self.label_9 = QtWidgets.QLabel(self.tasksWidget)
        self.label_9.setGeometry(QtCore.QRect(40, 330, 61, 16))
        self.label_9.setObjectName("label_9")
        self.createTaskButton = QtWidgets.QPushButton(self.tasksWidget)
        self.createTaskButton.setGeometry(QtCore.QRect(110, 500, 111, 23))
        self.createTaskButton.setObjectName("createTaskButton")
        self.markTaskAsDoneButton = QtWidgets.QPushButton(self.tasksWidget)
        self.markTaskAsDoneButton.setGeometry(QtCore.QRect(0, 250, 161, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markTaskAsDoneButton.setIcon(icon2)
        self.markTaskAsDoneButton.setObjectName("markTaskAsDoneButton")
        self.deleteTaskButton = QtWidgets.QPushButton(self.tasksWidget)
        self.deleteTaskButton.setGeometry(QtCore.QRect(400, 280, 151, 23))
        self.deleteTaskButton.setIcon(icon)
        self.deleteTaskButton.setObjectName("deleteTaskButton")
        self.markTaskAsNotDoneButton = QtWidgets.QPushButton(self.tasksWidget)
        self.markTaskAsNotDoneButton.setGeometry(QtCore.QRect(170, 250, 181, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markTaskAsNotDoneButton.setIcon(icon3)
        self.markTaskAsNotDoneButton.setObjectName("markTaskAsNotDoneButton")
        self.saveTaskButton = QtWidgets.QPushButton(self.tasksWidget)
        self.saveTaskButton.setGeometry(QtCore.QRect(400, 250, 151, 23))
        self.saveTaskButton.setIcon(icon1)
        self.saveTaskButton.setObjectName("saveTaskButton")
        self.aboutWidget = QtWidgets.QWidget(self.centralwidget)
        self.aboutWidget.setGeometry(QtCore.QRect(110, 80, 361, 221))
        self.aboutWidget.setObjectName("aboutWidget")
        self.label_11 = QtWidgets.QLabel(self.aboutWidget)
        self.label_11.setGeometry(QtCore.QRect(30, 120, 311, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.aboutWidget)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.closeAboutButton = QtWidgets.QPushButton(self.aboutWidget)
        self.closeAboutButton.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.closeAboutButton.setObjectName("closeAboutButton")
        self.label_12 = QtWidgets.QLabel(self.aboutWidget)
        self.label_12.setGeometry(QtCore.QRect(150, 40, 81, 81))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.categoriesWidget.raise_()
        self.aboutWidget.raise_()
        self.tasksWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        self.menuTask = QtWidgets.QMenu(self.menubar)
        self.menuTask.setObjectName("menuTask")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuCategory = QtWidgets.QMenu(self.menubar)
        self.menuCategory.setObjectName("menuCategory")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.viewTasksAction = QtWidgets.QAction(MainWindow)
        self.viewTasksAction.setObjectName("viewTasksAction")
        self.viewAllRatingsAction = QtWidgets.QAction(MainWindow)
        self.viewAllRatingsAction.setObjectName("viewAllRatingsAction")
        self.addTaskAction = QtWidgets.QAction(MainWindow)
        self.addTaskAction.setObjectName("addTaskAction")
        self.loginAction = QtWidgets.QAction(MainWindow)
        self.loginAction.setObjectName("loginAction")
        self.logoutAction = QtWidgets.QAction(MainWindow)
        self.logoutAction.setVisible(False)
        self.logoutAction.setObjectName("logoutAction")
        self.viewDocsAction = QtWidgets.QAction(MainWindow)
        self.viewDocsAction.setObjectName("viewDocsAction")
        self.viewAboutAction = QtWidgets.QAction(MainWindow)
        self.viewAboutAction.setObjectName("viewAboutAction")
        self.viewCategoriesAction = QtWidgets.QAction(MainWindow)
        self.viewCategoriesAction.setObjectName("viewCategoriesAction")
        self.addCategoryAction = QtWidgets.QAction(MainWindow)
        self.addCategoryAction.setObjectName("addCategoryAction")
        self.exportTasksToFile = QtWidgets.QAction(MainWindow)
        self.exportTasksToFile.setObjectName("exportTasksToFile")
        self.menuTask.addAction(self.viewTasksAction)
        self.menuTask.addAction(self.exportTasksToFile)
        self.menuHelp.addAction(self.viewAboutAction)
        self.menuCategory.addAction(self.viewCategoriesAction)
        self.menubar.addAction(self.menuTask.menuAction())
        self.menubar.addAction(self.menuCategory.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList - ???????????????????????? ???????????????? ??????????"))
        MainWindow.setAccessibleName(_translate("MainWindow", "???????????????????????? ???????????? ??????????"))
        self.categoriesDeleteButton.setText(_translate("MainWindow", "?????????????? ????????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????????? ??????????"))
        self.createCategoryButton.setText(_translate("MainWindow", "?????????????? "))
        self.label_2.setText(_translate("MainWindow", "?????? ??????????????????:"))
        self.label_3.setText(_translate("MainWindow", "???????????????????? ??????????????????"))
        self.saveCategoriesButton.setText(_translate("MainWindow", "??????????????????"))
        self.label_4.setText(_translate("MainWindow", "????????????"))
        self.label_5.setText(_translate("MainWindow", "???????????????? ????????????:"))
        self.label_6.setText(_translate("MainWindow", "????????????????????????"))
        self.label_7.setText(_translate("MainWindow", "????????????????"))
        self.label_8.setText(_translate("MainWindow", "???????? ????????????????????"))
        self.label_9.setText(_translate("MainWindow", "??????????????????"))
        self.createTaskButton.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.markTaskAsDoneButton.setText(_translate("MainWindow", "??????????????????"))
        self.deleteTaskButton.setText(_translate("MainWindow", "?????????????? ????????????????????"))
        self.markTaskAsNotDoneButton.setText(_translate("MainWindow", "???? ????????????????"))
        self.saveTaskButton.setText(_translate("MainWindow", "??????????????????"))
        self.label_11.setText(_translate("MainWindow", "  (??) 2022 ?????????? ???????????????? ????????????"))
        self.label_10.setText(_translate("MainWindow", "???????????????????????? ???????????????? ??????????"))
        self.closeAboutButton.setText(_translate("MainWindow", "??????????????"))
        self.menuTask.setTitle(_translate("MainWindow", "????????????"))
        self.menuHelp.setTitle(_translate("MainWindow", "????????????"))
        self.menuCategory.setTitle(_translate("MainWindow", "??????????????????"))
        self.viewTasksAction.setText(_translate("MainWindow", "?????? ????????????"))
        self.viewAllRatingsAction.setText(_translate("MainWindow", "?????? ????????????????"))
        self.addTaskAction.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.loginAction.setText(_translate("MainWindow", "????????"))
        self.logoutAction.setText(_translate("MainWindow", "??????????"))
        self.viewDocsAction.setText(_translate("MainWindow", "????????????????????????"))
        self.viewAboutAction.setText(_translate("MainWindow", "?? ??????????????????"))
        self.viewCategoriesAction.setText(_translate("MainWindow", "?????? ??????????????????"))
        self.addCategoryAction.setText(_translate("MainWindow", "???????????????? ??????????????????"))
        self.exportTasksToFile.setText(_translate("MainWindow", "?????????????????? ?? ????????"))
