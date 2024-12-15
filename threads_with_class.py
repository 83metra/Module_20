import threading
from PIL import Image
from datetime import datetime

import funcs


# dirname = 'dir_3'
working_time = None

class ImageToPdf(threading.Thread):
    '''
    Класс, который делает конвертацию.
    Из переданного кортежа извлекаются имя и расширение файла.
    Сначала каждый файл уменьшается до определённого размера, затем конвертируется в pdf.
    '''

    def __init__(self, dirname, file):
        super().__init__()
        self.dirname = dirname
        self.filename = file[0]
        self.file_extention = file[1]

    def run(self):
        # print(f'Конвертация {self.filename}.{self.file_extention} в {self.filename}.pdf')
        image = Image.open(f'{self.dirname}/{self.filename}.{self.file_extention}')
        width, height = image.size
        new_height = 800
        resized_image = image.resize(((int(new_height * width / height)), new_height))
        resized_image.save(f'{self.dirname}/{self.filename}.pdf', format='PDF', quality=200)


def convert_files_to_pdf(dirname):
    '''
    Данная функция запускает потоки конвертации. Один поток - один файл.
    Список convert_list - это список объектов класса ImageToPdf, куда передаются кортежем
    имя файла и его расширение.
    Сначала запускаются потоки, конвертирующие файлы в формат pdf, затем все они сшиваются
    в один многостраничный pdf-файл, в котором число страниц соответствует числу файлов, прошедших конвертацию.
    :return: Ничего не возвращает
    '''
    convert_list = [ImageToPdf(dirname, filename) for filename in funcs.files_to_conversion_1(dirname).values()]
    global working_time
    start = datetime.now()
    for file_to_convert in convert_list:
        thread = file_to_convert
        thread.start()

    for thread in convert_list:
        thread.join()
    end = datetime.now()
    working_time = (end - start)