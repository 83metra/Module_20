import sqlite3
from datetime import datetime

# from models.sessions import BotSessions
# from models.downloaded_images import DownloadedImagesAsDocs
# from models.uploaded_pdfs import UploadedPdfs

database_name = 'database.db'
# session_database = 'models/data_base.db'
# def initiate_db():
#     connection = sqlite3.connect(database_name)
#     cursor = connection.cursor()
#
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Downloaded_Images(
#     id INTEGER PRIMARY KEY,
#     mime_type TEXT NOT NULL,
#     thumbnail TEXT NOT NULL,
#     thumb TEXT NOT NULL,
#     file_id TEXT NOT NULL,
#     file_unique_id TEXT NOT NULL,
#     file_size INTEGER NOT NULL
#     )
#     ''')
#
#     connection.commit()  # сохранение изменений
#     connection.close()

def initiate_db():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Downloaded_Images(
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    mime_type TEXT NOT NULL,
    thumbnail_id TEXT NOT NULL,
    thumb_id TEXT NOT NULL,
    file_id TEXT NOT NULL,
    file_unique_id TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    download_time TEXT NOT NULL
    )
    ''')

    connection.commit()  # сохранение изменений
    connection.close()




initiate_db()


def insert_data_into_database(doc_attributes):
    '''
    Добавляет в базу данных атрибуты переданного в бот файла
    '''
    file_name = doc_attributes['file_name']
    mime_type = doc_attributes['mime_type']
    thumbnail_id = doc_attributes['thumbnail']
    thumb_id = doc_attributes['thumb']
    file_id = doc_attributes['file_id']
    file_unique_id = doc_attributes['file_unique_id']
    file_size = doc_attributes['file_size']
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Downloaded_Images(file_name, mime_type, thumbnail_id, thumb_id, file_id, file_unique_id, file_size, download_time)'
        ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (file_name, mime_type, thumbnail_id, thumb_id, file_id, file_unique_id, file_size, datetime.now()))
    connection.commit()
    connection.close()

def get_image_from_bot(file_id):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute('SELECT file_name from Downloaded_Images WHERE file_id == ?', (file_id,))
    file = cursor.fetchone()[0]
    connection.close()
    return file

# def set_session(number_of_session):
#     connection = sqlite3.connect(session_database)
#     cursor = connection.cursor()
#     cursor.execute('INSERT INTO bot_sessions(number_of_session, session_started_at) VALUES (?, ?)',
#                    (number_of_session, datetime.now()))
#     connection.commit()
#     connection.close()
