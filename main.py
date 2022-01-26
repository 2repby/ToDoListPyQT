import sys, os, PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.viewMyRatingsAction.triggered.connect(self.viewRating)
        self.loginAction.triggered.connect(self.login)
        self.logoutAction.triggered.connect(self.logout)


    def run(self):
        self.label.setText("OK")


    def viewRating(self):
        self.label.setText("Rating")

    def login(self):
        self.logoutAction.setVisible(True)
        self.loginAction.setVisible(False)

    def logout(self):
        self.logoutAction.setVisible(False)
        self.loginAction.setVisible(True)

    def loadRating(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())