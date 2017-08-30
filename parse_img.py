# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
'''
Для работы с программой необходимо подготовить входные данные.
Для этого помещаем список ссылок во входной каталог.

Программа работает в однопоточном режиме
'''
# ----Переменные-----
folder_out = 'images'  # переменная каталога с картинками
folder_in = 'files_in'  # переменная каталога с входящими данными
file_data = 'url_img.txt'  # переменная для рабочего файла с урлами
path_file_data = os.path.join(folder_in, file_data)
msg_url = 'Данные отсутствуют.\
        \nСохраните список урлов в файле <{}>.\
        \nКаждый урл должен находиться на новой строке.'.format(path_file_data)


# функция чтения файлов из каталога и получения списка ссылок
def read_file(list_work_files, folder_in):
    # list_work_files = os.listdir(folder_in)
    for work_file in list_work_files:
        file_name = folder_in + '/' + work_file
        with open(file_name, 'r') as f_in:
            urls = f_in.readlines()
    if not len(urls):
        print(msg_url)
    return urls


# получение корректного урла с большой картинкой
def get_large_file(url):
    url = url.split('!')[0]
    return url


# запрос обьекта картинки
def get_file(url):
    r = requests.get(url, stream=True)
    return r


# получения имени большой картинки
def get_name(url):
    name = url.split('/')[-1].split('!')[-2]
    if not os.path.exists(folder_out):
        os.makedirs(folder_out)
    path = os.path.abspath(folder_out)
    print(name)
    return path + '/' + name


# ф-ф сохранения картинки в каталог
def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


# ф-я создания входного каталога и файла для сохранения урлов
def create_work_path(path_file_data, folder_in):
    if not os.path.exists(folder_in):
        os.mkdir(folder_in)
        print('Каталог <{}> создан.'.format(folder_in))
    if not os.path.exists(path_file_data):
        with open(path_file_data, 'w') as f:
            f.write('')
        # print(msg_url)


def main():
    create_work_path(path_file_data, folder_in)
    list_work_files = os.listdir(folder_in)
    urls = read_file(list_work_files, folder_in)
    for url in urls:
        save_image(get_name(url), get_file(get_large_file(url)))
    # read_file(folder_in)


if __name__ == '__main__':
    main()
