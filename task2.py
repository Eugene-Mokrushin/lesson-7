"""Программа поддерживает до 5 уровней глубины"""

import os

# Получаем списком назваия папок и файлов из config.yaml (пробелы обязательно должны учитываться,
# каждый уровень - 2 пробела
link = r'C:\Users\79150\Desktop\GeekBrains Projects\Основы языка Python — вебинар\hw7'
with open('config.yaml', 'r', encoding='utf-8') as file:
    rows = [row for row in file]

# Сохраняет глубинность погружения
levels_of_folders = []

# Для создания основной папки
less_or_more = -1
counter = 0
global main_link

# Основной код
for row in rows:

    # Генерирует путь к основной папке
    if counter == 0:
        row = row.strip()
        row = row.rstrip()
        row = row[:-1]
        main_link = fr'{link}\{row}'
    counter += 1

    # Высчитывает кол-во пробелов (ака глубину), потом приводит название в правильный вид
    num_of_spaces = row.count(' ')
    row = row.rstrip()
    row = row.strip()

    # 1 уровень глубины(основной файл my_project)
    if num_of_spaces == 0:
        levels_of_folders.append(row)
        row = row[:-1] # - в дальнейшем это обрезает ':'
        if not os.path.exists(main_link):
            os.mkdir(main_link)

    # 2 уровень глубины(settings, mainapp, authapp)
    if num_of_spaces == 2:
        row = row[:-1]
        levels_of_folders.append(row)
        if not os.path.exists(fr'{main_link}\{row}'):
            os.mkdir(fr'{main_link}\{row}')

    # 3 уровень глуины(dev.py, templates, views.py и тд.)
    if num_of_spaces == 4:
        if row[-1] != ':':
            try:
                file = open(fr'{main_link}\{levels_of_folders[-1]}\{row}', 'x')
            except FileExistsError:
                print(f'{row} уже сущетсвует')

        else:
            row = row[:-1]
            if not os.path.exists(fr'{main_link}\{levels_of_folders[-1]}\{row}'):
                try:
                    os.mkdir(fr'{main_link}\{levels_of_folders[-1]}\{row}')
                    levels_of_folders.append(row)
                except FileNotFoundError:
                    print(f'{row} уже сущетсвует')

    # 4 уровень глубины (mainapp, authapp)
    if num_of_spaces == 6:
        if row[-1] != ':':
            try:
                file = open(fr'{main_link}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}', 'x')
            except FileExistsError:
                print(f'{row} уже сущетсвует')
        else:
            row = row[:-1]
            if not os.path.exists(fr'{main_link}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}'):
                try:
                    os.mkdir(fr'{main_link}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}')
                    levels_of_folders.append(row)
                except FileNotFoundError:
                    print(f'{row} уже сущетсвует')

    # 5 уровень глубины(base.html, index.html)
    if num_of_spaces == 8:
        if row[-1] != ':':
            try:
                file = open(
                    fr'{main_link}\{levels_of_folders[-3]}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}', 'x')
            except FileNotFoundError:
                print(f'{row} уже сущетсвует')
        else:
            row = row[:-1]
            if not os.path.exists(
                    fr'{main_link}\{levels_of_folders[-3]}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}'):
                try:
                    os.mkdir(
                        fr'{main_link}\{levels_of_folders[-3]}\{levels_of_folders[-2]}\{levels_of_folders[-1]}\{row}')
                    levels_of_folders.append(row)
                except FileNotFoundError:
                    print(f'{row} уже сущетсвует')
