from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import dirname

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Быстрая конвертация')
        ],
        [
            KeyboardButton(text='Загрузить изображения для конвертации'),
            KeyboardButton(text='Конвертировать изображения в pdf')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

kb_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Конвертировать один файл'),
            KeyboardButton(text='Конвертировать все файлы')
        ]
    ], resize_keyboard=True
)

button_in_1 = InlineKeyboardButton(text='Выбрать папку', callback_data='convert_else')  # 111111111 - select
seldir = InlineKeyboardMarkup(inline_keyboard=[[button_in_1]], resize_keyboard=True)

select_way = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Потоки', callback_data='threads')],
        [InlineKeyboardButton(text='Многопроцессорность', callback_data='mltprocess')],
        [InlineKeyboardButton(text='Последовательно один за другим', callback_data='step_by_step')]
    ]
)

end_conversation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Конвертировать ещё изображения', callback_data='convert_else')],
        [InlineKeyboardButton(text='Объединить все pdf-файлы в многостраничный pdf', callback_data='multipdf')]
    ]
)

kb_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Выбрать один файл', callback_data='one')],
        [InlineKeyboardButton(text='Все файлы', callback_data='all')]
    ]
)

send_multipdf = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Скачать pdf', callback_data='download_pdf')],
        [InlineKeyboardButton(text='Конвертировать ещё изображения', callback_data='convert_else')]
    ], resize_keyboard=True
)

download_pdf_in_images = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f'Скачать pdf из папки {dirname}', callback_data='download_pdf_in_images')]
    ], resize_keyboard=True
)

download_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Скачать pdf', callback_data='download_one')]
    ], resize_keyboard=True
)

convert_in_folder_images = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Конвертировать загруженные изображения', callback_data='all')]
    ],
)
