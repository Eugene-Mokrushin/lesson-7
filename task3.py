"""Программа поддерживает до 5 уровней глубины"""

import os

# Получаем списком назваия папок и файлов из config.yaml (пробелы обязательно должны учитываться,
# каждый уровень - 2 пробела
link = r'C:\Users\79150\Desktop\GeekBrains Projects\Основы языка Python — вебинар\hw7'
with open('config.yaml', 'r', encoding='utf-8') as file:
    rows = [row for row in file]

# Сохраняет глубинность погружения
levels_of_folders = []
all_templates = []
ind_counter = []
# Для создания основной папки
less_or_more = -1
counter = 0
global main_link

# Для нахождения индексов
dictionary_of_files = {}
index = 0

# Создает словарь из файлов и папкок и их ключей (индексов в списке) - это нужно если templates повторяются
for i in rows:
    i = i.strip().rstrip()
    if i in dictionary_of_files:
        dictionary_of_files[i].append(index)
    else:
        dictionary_of_files[i] = [index]

    index += 1
get_ind = dictionary_of_files.get(r'templates:')

# Получает индексы всех файлов, что находятся в templates
for row in get_ind:
    temp = rows[row]
    all_templates.append(temp)
    num_of_spaces = temp.count(' ')
    n = 1
    try:
        while rows[row + n].count(' ') > num_of_spaces:
            all_templates.append(rows[row + n])
            ind_counter.append(rows.index(rows[row + n]))
            n += 1
    except IndexError:
        pass

# Соединяет индексы папки templates и все, что в них (тоже их индексы)
get_ind.extend(ind_counter)


def del_list_indexes(lst, id_to_del):
    """
    Удаляет элменты из списка всех указанных индексов

    :param lst:
    :param id_to_del:
    :return:
    """
    some_list = [i for j, i in enumerate(lst) if j not in id_to_del]
    some_list.pop()
    return some_list


rows = del_list_indexes(rows, get_ind)

# Основной код
for row in rows:
    ind = rows.index(row)
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
        row = row[:-1]
        if not os.path.exists(main_link):
            os.mkdir(main_link)

    # 2 уровень глубины(settings, mainapp, authapp)
    if num_of_spaces == 2 and row != 'templates:':
        row = row[:-1]
        levels_of_folders.append(row)
        if not os.path.exists(fr'{main_link}\{row}'):
            os.mkdir(fr'{main_link}\{row}')

    # 3 уровень глуины(dev.py, templates, views.py и тд.)
    if num_of_spaces == 4 and row != 'templates:':
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
    if num_of_spaces == 6 and row != 'templates:':
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
    if num_of_spaces == 8 and row != 'templates:':
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

# Работаем уже с templates
all_templates.pop(0)
all_templates_levels = []
main_link = fr'{main_link}\templates'

# В конце добавляем уже ко всему в my_project папку templates с файлами
if not os.path.exists(main_link):
    os.mkdir(main_link)
for template in all_templates:
    num_of_spaces = template.count(' ')
    template = template.rstrip().strip()
    if num_of_spaces == 6 and template != 'templates:':
        template = template[:-1]
        all_templates_levels.append(template)
        if not os.path.exists(fr'{main_link}\{template}'):
            os.mkdir(fr'{main_link}\{template}')
    if num_of_spaces == 8 and template != 'templates:':
        try:
            file = open(fr'{main_link}\{all_templates_levels[-1]}\{template}', 'x')
        except FileExistsError:
            print(f'{template} уже сущетсвует')

print('End')


# Александр я не понял смысл задания от слова совсем, и даже после того насколько я понял (а скорее всего я понял суть
# неправильно) очень много ненужных костылей накидал. Если бы задача авторами методички было поставлена более точно,
# может получилось бы лучше. А решать то что я сам себе надумал и так у меня забрало все силы. Так что заместо
# красивого решения я нарисую домовенка

# ╰╰╲╲╲╲╲╲╳┃┃╱╱╮┈
# ╰╲╲╳╳╱╱╳╱╳╲╳╭╮┈
# ┈╱╱╭━╮┈╭━╮╱╱╲╲┈
# ╱╱▏┃▉┃┈┃▉┃▕╲╲▏▏
# ╱╱▏╭━╯┈╰━╯▕╲▏╲▏
# ╱╱╲╰━━╯┈┈┈▕╲╳╲▏
# ┈╱╱╲┈▔▔┈┈┈╱╲╲┈┈
