import threading
import requests
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# Подключаем окно
Form, Window = uic.loadUiType("update.ui")  #*!Изменить
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
    def down(nomer, url):
        print(str(nomer) + 'поток ('+url+')\n')
        (dirname, filename) = os.path.split(url)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
           with open(filename, 'wb') as f:
                r.raw.decode_content = True
           print(str(nomer) + "поток закончил загрузку\n")

    urls = ["https://codeload.github.com/NeodekvatDayz/TestUpdate/zip/refs/heads/main"]

    for nomer, url in enumerate(urls):
        threading.Thread(target=down, args=[nomer+1,url]).start()
    print("Скачиваем файлы...")
    #os.startfile('Open.bat')
    pass

# Назначаем функции виджетов
form.But.clicked.connect(chek)   
form.But2.clicked.connect(download)     

# Запуск окна
app.exec_()