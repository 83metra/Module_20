from config import *
import mltprocess
import funcs
import threads_with_class


# start = 'Бот-конвертер приветствует Вас!\nВыберите ниже:'

text_about = ('Загрузите изображения, чтобы получить затем конвертированный pdf-документ. '
              'Файлы загружаются в папку по умолчанию, затем можно выбрать либо один файл для конвертации, '
              'либо конвертировать сразу всю папку, получив на выходе многостраничный файл pdf.\n'
              'Также есть несколько папок на выбор, где уже лежат изображения. В папке dir_2 есть изображения размером в 10 МБ,'
              'на примере этой папки можно хорошо увидеть преимущества непоследовательного способа конвертации\n'
              'После того, как выгружен итоговый файл pdf, настройки сбрасываются, файлы из директории для загрузки удалятся,'
              'бот готов к следущему циклу конвертации.\n'
              'Поддерживаемыe типы изображений: jpb, bmp, png.')

select_dir = 'Выберите папку, осторожно кликнув в индекс с номером:'

wrong_dirname = 'Вы неправильно ввели имя папки!'

select_way_of_conv = 'Выберите действие:'

image_as_document = 'Для конвертации загружайте фото как документ, без сжатия!'

# select_file_in_dir = f"Выберите файл в директории {dirname}:"

# no_images_in_dir = 'В папке 📂 %s нет изображений, выберите другую.' % (dirname)

# converting_file_in_dir = f"Конвертируем файл {database_name[0]}.{database_name[1]} в папке 📂 {dirname}."

# converted_file_is_ready = f"Файл {database_name[0]}.pdf в папке 📂 {dirname} готов!"

# file_is_missing = f'Такого файла в папке 📂 {dirname} нет!'

# select_way_of_conf_in_dir = f'Выберите способ концертации файлов в папке 📂 {dirname}:'

# conv_all_with_threads = f'Конвертация всех файлов в папке 📂 {dirname} с использованием потоков...'

# conv_all_with_threads_is_ready = f'Конвертация в папке 📂 {dirname} завершена!\n'
#                                   f'Время работы:\n{threads_with_class.working_time}'

# conv_all_with_mltprocess = f'Конвертация всех файлов в папке 📂 {dirname} с использованием многопроцессорности...'

# conv_all_with_mltprocess_is_ready = (f'Конвертация всех файлов в папке 📂 {dirname} завершена!\n'
#                                      f'Время работы:\n ')


# conv_all_step_by_step = f'Конвертация файлов в папке 📂 {dirname} последовательно...'

# conv_all_step_by_step_is_ready = (f'Конвертация всех файлов в папке 📂 {dirname} завершена!\n'
#                                   f'Время работы:\n')

# all_pdf_merged = f"Всё файлы собраны в 'all_files_from({dirname}).pdf'"

# only_image_in_full_size = (f"Загружайте изображения как документ. "
#                            f"Все изображения будут загружены в папку 📂 {default_dir}, "
#                            f"когда будете готовы, нажмите кнопку под сообщением.")

# sending_merged_pdf = f"Загружаем многостраничный pdf из папки 📂 {dirname}..."
