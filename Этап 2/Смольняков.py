import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, \
    QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem
from PySide2.examples.widgets.itemviews.addressbook.tablemodel import TableModel


class QTDesign(QWidget):

    def __init__(self):
        # Возвращаем родительский объект QTDesign с классом и вызывем его конструктор
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создание кнопок
        self.ok_button = QPushButton("Готово")
        self.cancel_button = QPushButton("Закрыть")

        # Создаем пространство
        self.qspacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Создание меток для ввода языка и степени изучения
        self.label_language = QLabel("Введите язык: ")
        self.label_level = QLabel("Введите степень изучения: ")

        # Создание полей для ввода языка и степени изучения
        self.line_edit_language = QLineEdit()
        self.line_edit_level = QLineEdit()

        # Создание диалогового окна
        self.dialog = QMessageBox()
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(('Язык', 'Степень изучения'))
        self.data = [
            ['Python', 'Да'],
            ['Java', 'Да'],
            ['SQL', 'Да']
        ]
        row = 0
        for tup in self.data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.table.setItem(row, col, cellinfo)
                col += 1
            row += 1



        # Привязываем кнопки к функциям
        self.ok_button.clicked.connect(self.press_button)
        self.cancel_button.clicked.connect(self.close)

        # Создаем горизонтальный виджет и добавляем кнопки
        hbox = QHBoxLayout()
        hbox.addStretch(4)
        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)
        hbox.addItem(self.qspacer)

        # Создаем горизонтальный виджет и добавляем метку и поле для ввода логина
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.table)
        hbox2.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Создаем горизонтальный виджет добавляем метку и поле для ввода пароля
        hbox3 = QHBoxLayout()
        hbox3.addStretch(3)
        hbox3.addWidget(self.label_language)
        hbox3.addWidget(self.line_edit_language)
        hbox3.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        hbox4 = QHBoxLayout()
        hbox3.addStretch(2)
        hbox3.addWidget(self.label_level)
        hbox3.addWidget(self.line_edit_level)
        hbox3.addItem(QSpacerItem(100, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Создаем вертикальный виджет
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox)

        # Добавляем все боксы в основное окно
        self.setLayout(vbox)
        self.setGeometry(500, 300, 500, 300)
        self.setWindowTitle('Графический интерфейс')
        self.show()

    # Создаем функцию нажатия кнопки готово(при нажатии она вызывается)
    def press_button(self):
        language = self.line_edit_language.text()  # Получаем язык из поля ввода
        level = self.line_edit_level.text()  # Получаем степень из поля ввода
        self.data.append([str(language), (level)])
        print(self.data)
        self.dialog.setIcon(QMessageBox.Information)  # Создаем информационное окно
        self.dialog.setWindowTitle("Проверка")  # Добавляем ему название
        self.dialog.setText(language + ' ' + level)  # Загружаем в лего полученные данные
        self.dialog.exec_()  # Выводим на экран

    # Создаем функцию нажатия кнопки закрыть(при нажатии окно закрывается)
    def close(self):
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTDesign()
    sys.exit(app.exec_())
