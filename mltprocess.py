import multiprocessing
from PIL import Image
import funcs
from datetime import datetime
import os

core = os.cpu_count()
working_time = None
count_of_files = None

def convert_to_pdf(image_path):
    '''
    Функция конвертирует изображения в файл pdf, принимая путь до файла
    '''
    image = Image.open(f'{image_path[0]}/{image_path[1]}.{image_path[2]}')
    width, height = image.size
    new_height = 800
    resized_image = image.resize(((int(new_height * width / height)), new_height))
    resized_image.save(f'{image_path[0]}/{image_path[1]}.pdf', format='PDF', quality=200)


# if __name__ == '__main__':

def convert_files(dirname):
    '''
    Функция принимает имя папки, где нужно конвертировать изображения, далее создаёт список файлов, который передаётся
    в функцию многопроцессорности
    '''
    global working_time
    global count_of_files
    start = datetime.now()
    with multiprocessing.Pool(processes=core) as pool:
        all_images = []
        for name in funcs.files_to_conversion_1(dirname).values():
            all_images.append((dirname, name[0], name[1]))
        count_of_files = len(all_images)
        pool.map(convert_to_pdf, all_images)

    end = datetime.now()
    working_time = (end - start)
