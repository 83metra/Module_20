from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Начальные установки папок и имён файлов для конвертации
default_dir = 'images'
dirname = None
filename = None
filedict = {}
dirlist = []

images_extentions = ['.jpg', '.jpe', '.jfif', '.jpeg', '.png', '.bmp']

