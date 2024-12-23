# Module_20
Модуль 20. Завершающий. Дипломный.

Телеграм-бот на основе библиотеки aiogram как пример асинхронного программирования.
Этот телеграм-бот конвертирует изображения в формат pdf. Изображения можно как загрузить во временную папку и конвертировать их,
как и конвертировать имеющиеся файлы из других папок.
Для конвертации используются три разных способа:
    - Для конвертации одного файла используется простая функция.
    - Для конвертации большого числа файлов можно выбрать три способа для демонстрации их особенностей:
        - Конвертация последовательно один файл за другим. Такой способ самый медленный.
        - Способ с использованием многопроцессорности.
        - Способ с использованием потоков, где один поток конвертирует один файл

Особенность бота в том, что он принимает изображения только в виде документов.
Как один из примеров практического применения бота тогда - объединение в один многостраничный pdf нотный материал.
Изображения с нотами чувствительны к сжатию, поэтому нет смысла объединять в pdf изображения плохого качества.
Другой пример - документ можно сфотографировать на телефон и отправить боту, взамен он пришлёт объединённый pdf-документ.


ВВЕДЕНИЕ

1.1 Одно из основных направлений использования асинхронного программирования является написание телеграм-ботов с использованием библиотеки aiogram.
1.2 Написать телеграм-бот с использованием асинхронного программирования, который использовал бы многопоточность для одновременной конвертации изображений в документ pdf.



ОСНОВНЫЕ ПОНЯТИЯ И ОПРЕДЕЛЕНИЯ

Aiogram – библиотека, работающая асинхронным методом, который позволяет не останавливать работу телеграм-бота во время ожидания ответа от пользователя.

Bot -  отвечает за взаимодействие с пользователем в чате, а именно за стандартные реакции на его различные действия, являясь основой любого телеграм-бота.

Хендлер – функция-декоратор, которая нужна для обработки сообщений и действий от пользователя. Сообщения обрабатываются хендлером message_handler.

Инлайн-клавиатура – кнопки под сообщением, выводимым телеграм-ботом, с определёнными функциями, возврат которых перехватывается специальными хендлерами callback_query_handler


StatesGroup – класс, от которого наследуются классы, в которых определяются переменные для присвоения им определённых данных. Эти значения этих переменных перехватываются message_handler, принимающими значение state, равное переменной наследующего класса.

Мультипоточное программирование – способ, при котором операции выполняются параллельно в рамках одного процесса.


СТРУКТУРА ПРОЕКТА

| /dir_1 - папка с текстовым файлом (не изображением)
| /dir_2 - папка с одним изображением размером 9 МБ. Сделайте 128 его копий, чтобы проверить работу разных способов конвертации
| /dir_3 - папка с 10 изображениями
| — main.py – программный код с основной логикой телеграм-бота. Все хендлеры и оборачиваемые ими функциями прописаны именно здесь
| — config.py – файл с параментрами бота, диспетчера, а также установками имён файлов и директорий для загрузки. Также там находится  
| — keyboards.py - клавиатуры для телеграм-бота.
| — funcs.py – вспомогательные функции для телеграм-бота.
| — threads_with_class.py – функция, реализующая логику потоков на классе
| — mltprocess.py – функция, реализующая многопроцессорное программирование
| — texts.py – некоторые тексты для телеграм-бота
| — requirements.txt - файл зависимостей
| — crud_functions.py - функции по добавлению в бд данных о загруженных в бот файлах


ЗАДАЧИ ПРОЕКТА И ВЫВОДЫ

Определение наиболее оптимального способа конвертации множественного числа изображений при минимальном времени.

РАБОТА ПРИЛОЖЕНИЯ
1. Начало работы, бот запущен, введена команда /start, затем выбрана кнопка "Информация". 
![Начало работы](https://github.com/user-attachments/assets/2d4544b7-5d7c-441f-a046-df274aed02de)

2. Выбрано "Конвертировать изображения", бот предлагает папки на выбор. Папка images является папкой по умолчанию.
![Выбор папки](https://github.com/user-attachments/assets/48c83bdb-108c-4212-9274-e8aa8f6fe534)

3. Выбрана папка dir_2 под порядковым индексом /3. В ней находится 128 изображений каждое размером 9 МБ. 

![Выбрана папка 3](https://github.com/user-attachments/assets/e645c743-4162-4496-b137-99e0248ed81c)

4. Файлы в папке dir_2 конвертированы с помощью потоков и объединены в один многостраничный pdf.
![Файлы конвертированы с помощью потоков](https://github.com/user-attachments/assets/4b93d897-6751-432b-ab0a-df0ca32302a5)

5. Файлы в папке dir_2 конвертированы последовательно один за другим.
![Файлы конвертированы последовательно](https://github.com/user-attachments/assets/8f919e49-3316-4fa5-a7ad-3402c28143c3)

6. Файлы в папке dir_2 конвертированы с применением многопроцессороного подхода.
![Файлы конвертированы многопроцессорно](https://github.com/user-attachments/assets/9d37bad4-d0bf-4895-af3d-ee8858e006f4)

7. Выбор на клавиатуре "Загрузить изображения для конвертации".
![Выбор загрузки для конвертации](https://github.com/user-attachments/assets/f7dff253-c32c-4d2e-a1e1-2278f5ff1c27)

8. Изображение загружено в папку по умолчанию.
![Файл загружен в папку по умолчанию](https://github.com/user-attachments/assets/26ed76b8-3ab6-4da8-93af-4cc9d1721cea)

9. Выбор одного изображения для конвертации в папке по умолчанию.
![Выбор одного изображения в папке по умолчанию](https://github.com/user-attachments/assets/7819986b-07d8-45e2-a235-5b0caf5305e0)

10. Бот выгрузил конвертированный pdf-файл. Цикл завершился, все настройки сброшены к изначальным, все файлы из папки по умолчанию удалены,
    можно снова загружать и конвертировать.
![Бот выгрузил pdf-файл](https://github.com/user-attachments/assets/784aea87-fd20-4975-b39c-57efa439dda8)

11. Можно также выбрать быструю конвертацию, тогда на загрузку изображения бот будет отвечать выгрузкой конвертированного в pdf файла.
![Быстрая конвертация](https://github.com/user-attachments/assets/2adbd44a-4026-48e6-803f-7ef222b8b20e)

12. Бот выгрузил в ответ конвертированный pdf файл
![Быстрая конвертация - pdf получен](https://github.com/user-attachments/assets/a4d1980b-3dd1-4907-90c3-680cb897601a)

 





