import os

link = r'C:\Users\79150\Desktop\GeekBrains Projects\Основы языка Python — вебинар\hw7'


def create_project_template(link_for_folder):
    """
    Создает заготовку из папок для проекта по указанному пути

    :param link_for_folder:
    :return:
    """

    # Создаем основную папку
    main_dir_name = 'my_project'
    deeper_link = fr'{link_for_folder}\{main_dir_name}'
    if not os.path.exists(deeper_link):
        os.mkdir(main_dir_name)

    # Создаем папки внутри основной папки
    follow_up_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
    for dirs in follow_up_dirs:
        follow_up_link = fr'{deeper_link}\{dirs}'
        if not os.path.exists(follow_up_link):
            os.mkdir(follow_up_link)


create_project_template(link)

# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

# Да, можно. Простодописываем нужные новые папки в список
