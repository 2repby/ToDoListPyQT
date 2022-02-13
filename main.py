import sys, os, PySide2, sqlite3, PyQt5, design, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from design import Ui_MainWindow
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.categoriesWidget.setVisible(False)
        self.tasksWidget.setVisible(False)
        self.tasksWidget.setVisible(False)
        self.aboutWidget.setVisible(True)
        self.closeAboutButton.clicked.connect(self.close_about)
        self.viewCategoriesAction.triggered.connect(self.view_categories)
        self.exportTasksToFile.triggered.connect(self.export_tasks_to_file)
        self.viewTasksAction.triggered.connect(self.view_tasks)
        self.viewAboutAction.triggered.connect(self.view_about)
        self.categoriesDeleteButton.clicked.connect(self.delete_categories)
        self.createCategoryButton.clicked.connect(self.create_category)
        self.saveCategoriesButton.clicked.connect(self.save_category)
        self.saveTaskButton.clicked.connect(self.save_tasks)
        self.markTaskAsDoneButton.clicked.connect(self.mark_task_done)
        self.markTaskAsNotDoneButton.clicked.connect(self.mark_task_not_done)
        self.createTaskButton.clicked.connect(self.create_task)
        self.deleteTaskButton.clicked.connect(self.delete_tasks)
        self.connection = sqlite3.connect("todolist.db")
        self.connection.execute("PRAGMA foreign_keys = 1")
        self.selectCategoryComboBoxModel = QStandardItemModel()
        self.selectCategoryComboBox.currentIndexChanged.connect(self.on_select_category_combobox_change)
        self.selectCategoryComboBox.setModel(self.selectCategoryComboBoxModel)
        self.currentCategoryId = None
        self.init_select_category_combobox()

    def close_about(self):
        self.aboutWidget.setVisible(False)

    def view_about(self):
        self.categoriesWidget.setVisible(False)
        self.tasksWidget.setVisible(False)
        self.aboutWidget.setVisible(True)

    def init_select_category_combobox(self):
        query = "SELECT * FROM category"
        res = self.connection.cursor().execute(query).fetchall()
        for idi, name in res:
            item = QStandardItem(name)
            item.setData(idi)
            self.selectCategoryComboBoxModel.appendRow(item)

    def on_select_category_combobox_change(self, row):
        item = self.selectCategoryComboBoxModel.item(row)
        self.currentCategoryId = item.data()

    def create_category(self):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO category (name) VALUES ('" + self.createCategoryLineEdit.text() + "')")
        self.connection.commit()
        self.view_categories()

    def view_categories(self):
        self.categoriesWidget.setVisible(True)
        self.tasksWidget.setVisible(False)
        self.aboutWidget.setVisible(False)
        query = "SELECT category.id, category.name, count(task.id)" \
                "FROM category LEFT JOIN task ON task.category_id = category.id GROUP BY category.id"
        res = self.connection.cursor().execute(query).fetchall()
        self.categoriesTableWidget.setColumnCount(3)
        self.categoriesTableWidget.hideColumn(0)
        self.categoriesTableWidget.setRowCount(len(res))
        self.categoriesTableWidget.setSelectionMode(2)
        self.categoriesTableWidget.setSelectionBehavior(1)
        self.categoriesTableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.categoriesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.categoriesTableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Категория'))
        self.categoriesTableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Количество задач (всего)'))
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.categoriesTableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def delete_categories(self):
        rows = list(set([i.row() for i in self.categoriesTableWidget.selectedItems()]))
        ids = [self.categoriesTableWidget.item(i, 0).text() for i in rows]
        names = [self.categoriesTableWidget.item(i, 1).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Удалить категории " + ", ".join(names) + "?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM category WHERE id IN (" + ", ".join('?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.view_categories()

    def save_category(self):
        for i in range(self.categoriesTableWidget.rowCount()):
            id = self.categoriesTableWidget.item(i, 0).text()
            name = self.categoriesTableWidget.item(i, 1).text()
            cur = self.connection.cursor()
            cur.execute("UPDATE category SET name = ? WHERE id = ?", (name, id))
            self.connection.commit()
        self.view_categories()

    def view_tasks(self):
        self.categoriesWidget.setVisible(False)
        self.tasksWidget.setVisible(True)
        self.aboutWidget.setVisible(False)
        query = "SELECT task.id, task.name, task.description, task.deadline, case when task.done = 1 then 'Да' else 'Нет' end as done, category.name" \
                " FROM category INNER JOIN task ON task.category_id = category.id"
        res = self.connection.cursor().execute(query).fetchall()
        self.taskTableWidget.setColumnCount(6)
        self.taskTableWidget.hideColumn(0)
        self.taskTableWidget.setRowCount(len(res))
        self.taskTableWidget.setSelectionMode(2)
        self.taskTableWidget.setSelectionBehavior(1)
        self.taskTableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.taskTableWidget.horizontalHeader().setStretchLastSection(True)
        self.taskTableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Задача'))
        self.taskTableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Описание'))
        self.taskTableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Deadline'))
        self.taskTableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Выполнено)'))
        self.taskTableWidget.setHorizontalHeaderItem(5, QTableWidgetItem('Категория'))
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.taskTableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                self.taskTableWidget.item(i, j).setTextAlignment(1)
        self.taskTableWidget.resizeRowsToContents()

    def create_task(self):
        id_category = self.currentCategoryId
        print("create: ", id_category)
        name = self.taskNameEdit.text()
        print("name: ", name)
        description = self.taskDescriptionEdit.toPlainText()
        print("desc: ", description)
        task_date = self.taskDateTimeEdit.text()
        print("date: ", task_date)
        cur1 = self.connection.cursor()
        cur1.execute("INSERT INTO task (name, description, deadline, category_id) VALUES (?, ?, ?, ?)",
                     (str(name), str(description), str(task_date), str(id_category)))
        self.connection.commit()
        self.view_tasks()

    def mark_task_done(self):
        rows = list(set([i.row() for i in self.taskTableWidget.selectedItems()]))
        ids = [self.taskTableWidget.item(i, 0).text() for i in rows]
        names = [self.taskTableWidget.item(i, 1).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Отметить задачи " + ", ".join(names) + " как выполненные ?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("UPDATE task SET done=1 WHERE id IN (" + ", ".join('?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.view_tasks()

    def mark_task_not_done(self):
        rows = list(set([i.row() for i in self.taskTableWidget.selectedItems()]))
        ids = [self.taskTableWidget.item(i, 0).text() for i in rows]
        names = [self.taskTableWidget.item(i, 1).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Отметить задачи " + ", ".join(names) + " как НЕ выполненные ?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("UPDATE task SET done=0 WHERE id IN (" + ", ".join('?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.view_tasks()

    def save_tasks(self):
        for i in range(self.tasksTableWidget.rowCount()):
            id = self.tasksTableWidget.item(i, 0).text()
            name = self.tasksTableWidget.item(i, 1).text()
            desc = self.tasksTableWidget.item(i, 1).text()
            cur = self.connection.cursor()
            cur.execute("UPDATE task SET name = ? WHERE id = ?", (name, id))
            self.connection.commit()
        self.view_tasks()

    def delete_tasks(self):
        rows = list(set([i.row() for i in self.taskTableWidget.selectedItems()]))
        ids = [self.taskTableWidget.item(i, 0).text() for i in rows]
        names = [self.taskTableWidget.item(i, 1).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Удалить задачи " + ", ".join(names) + "?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM task WHERE id IN (" + ", ".join('?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.view_tasks()

    def export_tasks_to_file(self):
        with open('tasks.csv', 'w', newline='') as csvfile:
            query = "SELECT task.id, task.name, task.description, task.deadline, "\
                    "case when task.done = 1 then 'Да' else 'Нет' end as done, category.name" \
                    " FROM category INNER JOIN task ON task.category_id = category.id"
            res = self.connection.cursor().execute(query).fetchall()
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['ID', 'Наименование', 'Описание', 'Срок выполнения', 'Выполнено (Да/Нет)', 'Категория'])
            for i, row in enumerate(res):
                filewriter.writerow(row)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
