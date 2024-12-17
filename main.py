from aiogram import executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import FileIsTooBig
import os

from aiogram.types import InputFile

import mltprocess
import threads_with_class
import funcs
from keyboards import *
from config import *
from texts import *


# aiogram==2.25.1


class PathAttr(StatesGroup):
    dirname = State()
    filename = State()


@dp.message_handler(commands='start')
async def hallo(message):
    await message.answer(start, reply_markup=kb)
    funcs.set_default_dir(default_dir)
    funcs.delete_all_files(default_dir)
    funcs.set_default()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer(text_about, reply_markup=kb)


@dp.message_handler(text='Конвертировать изображения в pdf')
async def privet(message):
    await message.answer(select_dir)
    for directory in funcs.get_dir():
        dirlist.append(directory)
        await message.answer(f'/{directory[0]}- 📂 папка: {directory[1]}')
        await PathAttr.dirname.set()


@dp.callback_query_handler(text='convert_else')
async def convert_else(call):
    funcs.set_default()
    await call.message.answer(select_dir)
    for directory in funcs.get_dir():
        dirlist.append(directory)
        await call.message.answer(f'/{directory[0]}- 📂 папка: {directory[1]}')
        await PathAttr.dirname.set()
    await call.answer()


@dp.callback_query_handler(text='one')
async def select_file(call):
    await call.message.answer(f"Выберите файл в директории {dirname}:")
    file_list = funcs.files_to_conversion_1(dirname)
    if len(file_list) > 0:
        for index, file in file_list.items():
            filedict.update({index: (file[0], file[1])})
            await call.message.answer(f'/{index} - {file[0]}.{file[1]}')
            await PathAttr.filename.set()
    else:
        await call.message.answer('В папке 📂 %s нет изображений, выберите другую.' % (dirname), reply_markup=seldir)
    await call.answer()


@dp.message_handler(state=PathAttr.filename)
async def convert_one_file(message, state):
    await state.update_data(filename=message.text)
    global filename
    awaited_filename = await state.get_data()
    for index, file in filedict.items():
        if str(index) == awaited_filename['filename'][1:] or awaited_filename['filename'] == f'{file[0]}.{file[1]}':
            filename = file
            await message.answer(f"Конвертируем файл {filename[0]}.{filename[1]} в папке 📂 {dirname}.")
            funcs.convert_one_file_to_pdf(dirname, filename)
            await message.answer(f"Файл {filename[0]}.pdf в папке 📂 {dirname} готов!", reply_markup=download_one)
            await state.finish()
            # funcs.delete_all_files(dirname)
    if filename is None:
        await message.reply(f'Такого файла в папке 📂 {dirname} нет!')


@dp.callback_query_handler(text='all')
async def convert_all_files(call):
    global dirname
    if dirname is None:
        dirname = default_dir
        file_list = funcs.files_to_conversion_1(dirname)
        if len(file_list) == 0:
            await call.message.answer('В папке 📂 %s нет изображений, выберите другую.' % (dirname), reply_markup=seldir)
            await call.answer()
        else:
            await call.message.answer(f'Выберите способ концертации файлов в папке 📂 {dirname}:',
                                      reply_markup=select_way)
            await call.answer()
    else:
        file_list = funcs.files_to_conversion_1(dirname)
        if len(file_list) == 0:
            await call.message.answer('В папке 📂 %s нет изображений, выберите другую.' % (dirname), reply_markup=seldir)
            await call.answer()
        else:
            await call.message.answer(f'Выберите способ концертации файлов в папке 📂 {dirname}:',
                                      reply_markup=select_way)
            await call.answer()


@dp.callback_query_handler(text='threads')
async def convert_using_threads(call):
    await call.message.answer(f'Конвертация всех файлов в папке 📂 {dirname} с использованием потоков...')
    threads_with_class.convert_files_to_pdf(dirname)
    await call.message.answer(f'Конвертация в папке 📂 {dirname} завершена!\n'
                              f'Время работы:\n{threads_with_class.working_time}', reply_markup=end_conversation)
    await call.answer()


@dp.callback_query_handler(text='mltprocess')
async def convert_using_multiprocessing(call):
    await call.message.answer(f'Конвертация всех файлов в папке 📂 {dirname} с использованием многопроцессорности...')
    mltprocess.convert_files(dirname)
    await call.message.answer(f'Конвертация всех файлов в папке 📂 {dirname} завершена!\n'
                              f'Время работы:\n {mltprocess.working_time}', reply_markup=end_conversation)
    await call.answer()


@dp.callback_query_handler(text='step_by_step')
async def convert_all_step_by_step(call):
    global dirname
    await call.message.answer(f'Конвертация файлов в папке 📂 {dirname} последовательно...')
    funcs.convert_all_files_to_pdf_synco(dirname)
    await call.message.answer(f'Конвертация всех файлов в папке 📂 {dirname} завершена!\n'
                              f'Время работы:\n{funcs.step_by_step_worktime}', reply_markup=end_conversation)


@dp.callback_query_handler(text='multipdf')
async def multipdf(call):
    funcs.pdf_merger(dirname)
    await call.message.answer(f"Всё файлы собраны в 'all_files_from({dirname}).pdf'",
                              reply_markup=send_multipdf)
    await call.answer()


@dp.message_handler(text='Загрузить изображения для конвертации')
async def upload_files_to_bot(message):
    global dirname
    dirname = default_dir
    await message.answer(f"Загружайте изображения как документ. "
                         f"Все изображения будут загружены в папку 📂 {dirname}, "
                         f"когда будете готовы, нажмите кнопку под сообщением.")


@dp.callback_query_handler(text='download_pdf')
async def sending_merged_pdf(call):
    global dirname
    await call.message.answer(f"Загружаем многостраничный pdf из папки 📂 {dirname}...")
    local_file_path = os.path.join(f'{dirname}', f"all_files_from({dirname}).pdf")
    response_file = InputFile(local_file_path)
    await call.message.reply_document(response_file, reply_markup=kb)
    await call.answer()
    funcs.set_default()


@dp.callback_query_handler(text='download_one')
async def download_one_file_pdf(call):
    global dirname
    global filename
    await call.message.answer(f"Загружаем файл '{filename[0]}.pdf' из папки 📂 {dirname}...")
    local_file_path = os.path.join(f'{dirname}', f"{filename[0]}.pdf")
    try:
        await call.message.reply(f'Ищем файл {filename[0]}.pdf...')
        response_file = InputFile(local_file_path)
        await call.message.reply_document(response_file, reply_markup=kb)
        await call.answer()
    except FileNotFoundError:
        await call.message.reply(f'Файла {filename[0]}.pdf в папке нет.\n'
                                 f'Скорее всего, он был загружен во временную папку 📂 {dirname}\n'
                                 f'Загружайте в неё изображения по одному и конвертируйте сразу.\n'
                                 f'Или загружайте сразу несколько и получите на выходе многостраничный pdf.')
    funcs.set_default()


@dp.message_handler(state=PathAttr.dirname)
async def select_action(message, state):
    await state.update_data(dirname=message.text)
    global dirname
    awaited_directory = await state.get_data()
    for name in dirlist:
        if str(name[0]) == (awaited_directory['dirname'][1:]) or name[1] == awaited_directory['dirname']:
            dirname = name[1]
    if dirname is None:
        await message.answer(wrong_dirname, reply_markup=seldir)
        await state.finish()
    else:
        await message.answer(select_way_of_conv, reply_markup=kb_2)
        await state.finish()



@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def download_image(message):
    photo = message.document
    if photo['mime_type'] == "image/jpeg":
        try:
            file_info = await bot.get_file(photo.file_id)
            # file_name = photo['file_name']
            file_name = funcs.filename_splitter(photo['file_name'])
            file_path = file_info.file_path
            if dirname == default_dir:
                await message.answer(f"Изображения загружены в папку  по умолчанию 📂 {dirname}.\n"
                                     f"Можно загрузить ещё файл, либо конвертировать.",
                                     reply_markup=kb_2)

                # бот сохраняет файл на диске
                local_file_path = os.path.join(f'{default_dir}', f"{file_name[0]}.{file_name[1]}")
                await bot.download_file(file_path, local_file_path)
            else:
                await message.answer(f"Изображения загружены в папку 📂 {dirname}. \n"
                                     f"Можно загрузить ещё, либо конвертировать.",
                                     reply_markup=convert_in_folder_images)

                # бот сохраняет файл на диске
                local_file_path = os.path.join(f'{default_dir}', f"{file_name[0]}.{file_name[1]}")
                await bot.download_file(file_path, local_file_path)
        except FileIsTooBig as e:
            await message.answer(f'Ошибка: {e}\nФайл слишком большой.')
    else:
        await message.answer('Кажется, Вы отправили что-то не то!..\nНужно отправить изображение как документ, не сжимая его!')

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    await message.answer(image_as_document)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
