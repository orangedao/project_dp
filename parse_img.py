# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from multiprocessing import Pool
'''
Для работы с программой необходимо подготовить входные данные.
Для этого помещаем список ссылок во входной каталог.

Программа работает в многопроцессорном режиме
'''
# ----Переменные-----
# folder_out = 'images'  # переменная каталога с картинками
# folder_in = 'files_in'  # переменная каталога с входящими данными
# file_data = 'url_img.txt'  # переменная для рабочего файла с урлами
# path_file_in = os.path.join(folder_in, file_data)
# msg_url = 'Данные отсутствуют.\
#         \nСохраните список урлов в файле <{}>.\
#         \nКаждый урл должен находиться на новой строке.'.format(path_file_in)


# функция чтения файлов из каталога и получения списка ссылок
def read_file(path_file_in):
    with open(path_file_in, 'r') as f_in:
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
    # if not os.path.exists(folder_out):
    #     os.mkdir(folder_out)
    path = os.path.join(folder_out, name)
    print(name)
    return path


# ф-ф сохранения картинки в каталог
def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


# ф-я создания входного каталога и пустого файла для сохранения урлов
def create_work_dirs(path_file_in, folder_in, folder_out):
    if not os.path.exists(folder_in):
        os.mkdir(folder_in)
        # print('Каталог <{}> создан.'.format(folder_in))
    if not os.path.exists(path_file_in):
        with open(path_file_in, 'w') as f:
            f.write('')
    if not os.path.exists(folder_out):
        os.mkdir(folder_out)


def make_all(url):
    save_image(get_name(url), get_file(get_large_file(url)))
    # pass


def main():
    create_work_dirs(path_file_in, folder_in, folder_out)
    urls = read_file(path_file_in)
    with Pool(10) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    folder_out = 'images'  # переменная каталога с картинками
    folder_in = 'files_in'  # переменная каталога с входящими данными
    file_data = 'url_img.txt'  # переменная для рабочего файла с урлами
    path_file_in = os.path.join(folder_in, file_data)
    msg_url = 'Данные отсутствуют.\
            \nСохраните список урлов в файле <{}>.\
            \nКаждый урл должен находиться на новой строке.'.format(path_file_in)

    main()
