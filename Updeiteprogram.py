from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# Подключаем окно
Form, Window = uic.loadUiType("panm.ui")  #*!Изменить
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

#Окно программы

#Проверка обновления
def chek():

    pass

#Обновление программы
def download():
    pass

# Назначаем функции виджетов
form.But.clicked.connect(chek)   
form.But2.clicked.connect(download)     

# Запуск окна
app.exec_()