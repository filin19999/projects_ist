import sys
from PyQt5.QtWidgets import QApplication, \
    QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QLabel, QLineEdit, QMessageBox


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

        # Создание меток для ввода логина и пароля
        self.label_name = QLabel("Введите логин: ")
        self.label_password = QLabel("Введите пароль: ")

        # Создание полей для ввода логина и пароля
        self.line_edit_name = QLineEdit()
        self.line_edit_password = QLineEdit()

        # Создание диалогового окна
        self.dialog = QMessageBox()

        # Привязываем кнопки к функциям
        self.ok_button.clicked.connect(self.press_button)
        self.cancel_button.clicked.connect(self.close)

        # Создаем горизонтальный виджет и добавляем кнопки
        hbox = QHBoxLayout()
        hbox.addStretch(3)
        hbox.addWidget(self.ok_button)
        hbox.addWidget(self.cancel_button)
        hbox.addItem(self.qspacer)

        # Создаем горизонтальный виджет и добавляем метку и поле для ввода логина
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label_name)
        hbox2.addWidget(self.line_edit_name)
        hbox2.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Создаем горизонтальный виджет добавляем метку и поле для ввода пароля
        hbox3 = QHBoxLayout()
        hbox3.addStretch(2)
        hbox3.addWidget(self.label_password)
        hbox3.addWidget(self.line_edit_password)
        hbox3.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Создаем вертикальный виджет
        vbox = QVBoxLayout()
        vbox.addStretch(1)
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
        login = self.line_edit_name.text()  # Получаем логин из поля ввода
        password = self.line_edit_password.text()  # Получаем логин из поля ввода
        self.dialog.setIcon(QMessageBox.Information)  # Создаем информационное окно
        self.dialog.setWindowTitle("Проверка")  # Добавляем ему название
        self.dialog.setText(login + ' ' + password)  # Загружаем в лего полученные данные
        self.dialog.exec_()  # Выводим на экран

    # Создаем функцию нажатия кнопки закрыть(при нажатии окно закрывается)
    def close(self):
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTDesign()
    sys.exit(app.exec_())
