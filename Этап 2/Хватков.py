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
        self.ok_button = QPushButton("Ок")

        # Создаем пространство
        self.qspacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Создание меток для ввода имени, фамилии и звания
        self.label_name = QLabel("Введите имя: ")
        self.label_surname = QLabel("Введите фамилию: ")
        self.label_rank = QLabel("Введите звание: ")

        # Создание полей для ввода логина и пароля
        self.line_edit_name = QLineEdit()
        self.line_edit_surname = QLineEdit()
        self.line_edit_rank = QLineEdit()

        # Создание диалогового окна
        self.dialog = QMessageBox()

        # Привязываем кнопки к функциям
        self.ok_button.clicked.connect(self.press_button)

        # Создаем горизонтальный виджет и добавляем кнопки
        hbox = QHBoxLayout()
        hbox.addStretch(3)
        hbox.addWidget(self.ok_button)
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
        hbox3.addWidget(self.label_surname)
        hbox3.addWidget(self.line_edit_surname)
        hbox3.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        hbox4 = QHBoxLayout()
        hbox4.addStretch(3)
        hbox4.addWidget(self.label_rank)
        hbox4.addWidget(self.line_edit_rank)
        hbox4.addItem(QSpacerItem(200, 500, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Создаем вертикальный виджет
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox)

        # Добавляем все боксы в основное окно
        self.setLayout(vbox)

        self.setGeometry(500, 300, 500, 300)
        self.setWindowTitle('Ввод')
        self.show()

    def closeEvent(self, event): #создаем событие при закрытии приложения

        reply = QMessageBox.question(self, 'Message',
                                     "Вы уверены что хотитие выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    # Создаем функцию нажатия кнопки готово(при нажатии она вызывается)
    def press_button(self):
        name = self.line_edit_name.text()  # Получаем имя из поля ввода
        surname = self.line_edit_surname.text() # Получаем фамилию из поля ввода
        rank = self.line_edit_rank.text() # Получаем звание из поля ввода
        self.dialog.setIcon(QMessageBox.Information)  # Создаем информационное окно
        self.dialog.setWindowTitle("Проверка")  # Добавляем ему название
        self.dialog.setText(rank + ' ' + name + ' ' + surname)  # Загружаем в него полученные данные
        self.dialog.exec_()  # Выводим на экран




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTDesign()
    sys.exit(app.exec_())
