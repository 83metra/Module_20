import os
from datetime import datetime

import main
# from threads_with_class import ImageToPdf
from PIL import Image
from PyPDF2 import PdfMerger

from config import default_dir, dirname, dirlist, filedict, images_extentions, mime_type_list

step_by_step_worktime = None


def get_dir():
    '''
    Функция составляет список папок, где каждой присваивается порядковый индекс
    :return: [(индекс, имя папки),]
    '''
    root_dir = [dirs for root, dirs, files in os.walk(os.getcwd())][0]
    # dirs = [dir for dir in root_dir if dir != '.venv' and dir != '.idea' and dir != '__pycache__']  # старая версия
    dirs = [dir for dir in root_dir if not dir.startswith('.') and not dir.startswith('_')]
    indexes = [index + 1 for index in range(len(dirs))]
    dirs_dist = list(zip(indexes, dirs))
    return dirs_dist


def set_default_dir(folder_path):
    '''
    Проверяет наличие папки по умолчанию, если отсутствует, то создаёт её.
    :param folder_path: имя папки по умолчанию
    :return: str(имя папки по умолчанию)
    '''
    if os.path.isdir(folder_path):
        return folder_path
    else:
        os.mkdir(folder_path)
        return folder_path


def files_to_conversion_1(dirpath):
    '''
    Функция отбирает все файлы изображений в заданной папке и создаёт словарь,
    который передаётся далее при создании объектов класса.
    :return: Возвращает словарь {'порядковый индекс': (имя файла, расширение файла)}
    '''
    files_to_convert = {}
    index = 0
    os.chdir(dirpath)
    files = sorted([files for root, dirs, files in os.walk('.')][0])
    for file in files:
        if file[-3:] == 'jpg':
            index += 1
            files_to_convert.update({index: (file[:-4], 'jpg')})
        elif file[-3:] == 'jpe':
            index += 1
            files_to_convert.update({index: (file[:-4], 'jpe')})
        elif file[-4:] == 'jfif':
            index += 1
            files_to_convert.update({index: (file[:-5], 'jfif')})
        elif file[-4:] == 'jpeg':
            index += 1
            files_to_convert.update({index: (file[:-5], 'jpeg')})
        elif file[-3:] == 'png':
            index += 1
            files_to_convert.update({index: (file[:-4], 'png')})
        elif file[-3:] == 'bmp':
            index += 1
            files_to_convert.update({index: (file[:-4], 'bmp')})
    os.chdir('../')
    return files_to_convert


def filename_splitter(filename):
    '''
    Фунцкия принимает имя файла, которое загружено через телеграм-бот (из словаря {'file_name': имя файла}),
    где оно является строкой. Функция разбивает его на имя файла и его расширение
    :return: кортеж ('имя файла', 'расширение файла')
    '''
    for name in images_extentions:
        if name in filename:
            return tuple(filename.split('.'))


def is_valid_mime_type(mime_type):
    '''
    Принимает значение по ключу 'mime_type' и проверяет соответствие со значением из списка mime_type_list
    :return: bool
    '''
    return bool([typ for typ in mime_type_list if typ == mime_type])


def convert_one_file_to_pdf(dirname, filename):
    '''
    Конвертирует одно изображение в pdf
    :param dirname: имя папки, где находится изображение
    :param filename: имя файла
    :return:
    '''
    image = Image.open(f'{dirname}/{filename[0]}.{filename[1]}')
    width, height = image.size
    new_height = 800
    resized_image = image.resize(((int(new_height * width / height)), new_height))
    resized_image.save(f'{dirname}/{filename[0]}.pdf', format='PDF', quality=200)


def convert_all_files_to_pdf_synco(dirname):
    '''
    Функция конвертирует все изображения в pdf последовательно
    :param dirname: имя папки с изображениями
    :return:
    '''
    global step_by_step_worktime
    start = datetime.now()
    for filename in files_to_conversion_1(dirname).values():
        image = Image.open(f'{dirname}/{filename[0]}.{filename[1]}')
        width, height = image.size
        new_height = 800
        resized_image = image.resize(((int(new_height * width / height)), new_height))
        resized_image.save(f'{dirname}/{filename[0]}.pdf', format='PDF', quality=200)
    step_by_step_worktime = (datetime.now() - start)


def pdf_merger(dirname):
    '''
    Собирает все файлы pdf в директории в один многостраничный файл
    :param dirname:
    :return:
    '''
    book = PdfMerger()
    for file in files_to_conversion_1(dirname).values():
        pdf = f'{dirname}/{file[0]}.pdf'
        book.append(pdf)
    book.write(f'{dirname}/all_files_from({dirname}).pdf')
    book.close()


def set_default():
    '''
    Сбрасывает все настройки к начальным после завершения цикла конвертации
    :return:
    '''
    global dirname
    global filename
    global filedict
    global dirlist
    dirname, filename, filedict, dirlist = None, None, {}, []


def delete_all_files(dirname):
    '''
    Если имя папки совпадает с папкой, куда по умолчанию загружаются изображения,
    то оттуда удаляются все файлы по окончании цикла конвертации все файлы
    :param dirname: имя папки, где лежат изображения для конвертации
    :return:
    '''
    if dirname == default_dir:
        for filename in os.listdir(dirname):
            file_path = os.path.join(dirname, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f'При удалении файла ошибка: {file_path}. {e}')
