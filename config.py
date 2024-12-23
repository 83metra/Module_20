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
blitz = False

# Расширения принимаемых изображений и список mim_type'о.
images_extentions = ['.jpg', '.jpe', '.jfif', '.jpeg', '.png', '.bmp']
mime_type_list = ["image/jpeg", "image/bmp", "image/png"]
