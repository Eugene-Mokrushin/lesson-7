import os


# Основной код
def get_size_of_folder(link):
    sizes = {}
    zero = 0
    extensions_zero = []
    hundred = 0
    extensions_hundred = []
    thousand = 0
    extensions_thousand = []
    ten_thousand = 0
    extensions_ten_thousand = []
    hundred_thousand = 0
    extensions_hundred_thousand = []

    # Получаем все из папки но работаем только с файлами
    for adress, dirs, files in os.walk(link):
        for file in files:
            file = fr'{adress}\{file}'
            if 100 < os.stat(file).st_size < 1000:
                hundred += 1
                extensions_file_list = file.split('.')
                extensions_hundred.append(extensions_file_list[-1])
                extensions_hundred = list(set(extensions_hundred))
            elif 1000 < os.stat(file).st_size < 10000:
                thousand += 1
                extensions_file_list = file.split('.')
                extensions_thousand.append(extensions_file_list[-1])
                extensions_thousand = list(set(extensions_thousand))
            elif 10000 < os.stat(file).st_size < 100000:
                ten_thousand += 1
                extensions_file_list = file.split('.')
                extensions_ten_thousand.append(extensions_file_list[-1])
                extensions_ten_thousand = list(set(extensions_ten_thousand))
            elif 100000 < os.stat(file).st_size:
                hundred_thousand += 1
                extensions_file_list = file.split('.')
                extensions_hundred_thousand.append(extensions_file_list[-1])
                extensions_hundred_thousand = list(set(extensions_hundred_thousand))
            else:
                zero += 1
                extensions_file_list = file.split('.')
                extensions_zero.append(extensions_file_list[-1])
                extensions_zero = list(set(extensions_zero))

    # Добавляем все в словарь
    sizes[0] = zero, extensions_zero
    sizes[100] = hundred, extensions_hundred
    sizes[1000] = thousand, extensions_thousand
    sizes[10000] = ten_thousand, extensions_ten_thousand
    sizes[100000] = hundred_thousand, extensions_hundred_thousand

    return sizes


# Сюда мы вставляем прямую ссылку на файл, который хотим просканировать
measure_size_link = r'C:\Users\79150\Desktop\GeekBrains Projects'

# Получем размеры файлов и название папки которую сканируем
all_sizes = (get_size_of_folder(measure_size_link))
folder_name = os.path.basename(measure_size_link)

# Выводит в консоль что получилось по размерам
for size in all_sizes:
    print(size, all_sizes.get(size))

# Здесь вставляем ссылку куда будет создан json файл
link_of_saving = r'C:\Users\79150\Desktop\GeekBrains Projects\Основы языка Python — вебинар\hw7'
# Здесь мы либо перезаписывем json файл, либо создаем и записываем в него
try:
    with open(fr'{link_of_saving}\{folder_name}_summary.json', 'x', encoding='utf-8') as file:
        for size in all_sizes:
            file.write(f'{size}: {all_sizes.get(size)} \n')
except FileExistsError:
    with open(fr'{link_of_saving}\{folder_name}_summary.json', 'w', encoding='utf-8') as file:
        for size in all_sizes:
            file.write(f'{size}: {all_sizes.get(size)} \n')

# Александр, я только в конце еще раз перечитал задание и понял что там файлы до 100 байт записываются не в 0, а в 100
# Но я думаю суть та же, да?
