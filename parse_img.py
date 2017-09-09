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
# Переменные
folder_out = 'images'  # переменная каталога с картинками
# folder_out = input('Введите название каталога: ')

folder_in = 'files_in'  # переменная каталога с входящими данными
file_data = 'url_img.txt'  # переменная для рабочего файла с урлами
path_file_in = os.path.join(folder_in, file_data)  # полный путь до файла со списком картинок
msg_url = 'Данные отсутствуют.\
            \nСохраните список урлов в файле <{}>.\
            \nКаждый урл должен находиться на новой строке.'.format(path_file_in)


# функция чтения файлов из каталога и получения списка ссылок на маленькие картинки
def read_file(path_file_in):
    with open(path_file_in, 'r') as f_in:
        urls_small_img = f_in.readlines()
    if not len(urls_small_img):
        print(msg_url)
    return urls_small_img  # список урлов с маленькими картинками


# получение корректного урла с большой картинкой
def get_large_file(url_small_img):
    url_big_img = url_small_img.split('!')[0]
    return url_big_img


# запрос обьекта большой картинки
def get_file(url_big_img):
    r = requests.get(url_big_img, stream=True)
    return r


# получение имени большой картинки
def get_name_big_img(url_small_img):
    name_big_img = url_small_img.split('/')[-1].split('!')[0]
    # name_artist = url.split('/')[-2]
    # artist_dir = os.path.join(folder_out, name_artist)
    # if not os.path.exists(artist_dir):
    #     os.mkdir(artist_dir)
    # path_big_img = os.path.join(folder_out, name_big_img)
    return name_big_img  # имя большой картинки


# получение имени автора(имя подкаталога)
def get_name_author(url_small_img):
    name_author = url_small_img.split('/')[-2]
    author_dir = os.path.join(folder_out, name_author)
    if not os.path.exists(author_dir):
        os.mkdir(author_dir)
    return author_dir


# получение полного пути до большой картинки
def get_full_path_big_img(folder_out, author_dir, name_big_img):
    full_path_big_img = os.path.join(folder_out, author_dir, name_big_img)
    # print('путь до картинки' + full_path_big_img)
    return full_path_big_img


# ф-ф сохранения большой картинки в каталог
def save_image(full_path_big_img, file_big_img):
    with open(full_path_big_img, 'bw') as f:
        for chunk in file_big_img.iter_content(8192):
            f.write(chunk)
    print('Файл <{}> сохранен'.format(full_path_big_img))


# ф-я создания входного и выходного каталогов и пустого файла для сохранения урлов
def create_work_dirs(path_file_in, folder_in, folder_out):
    if not os.path.exists(folder_in):
        os.mkdir(folder_in)
    if not os.path.exists(path_file_in):
        with open(path_file_in, 'w') as f:
            f.write('')
    if not os.path.exists(folder_out):
        os.mkdir(folder_out)


# вспомогательная ф-я для запуска в  многопроцесорном режиме
# параметр url_small_img и переменная url_small_img - урл одной маленькой картинки
def make_all(url_small_img):
    author_dir = get_name_author(url_small_img)
    name_big_img = get_name_big_img(url_small_img)
    save_image(get_full_path_big_img(folder_out, author_dir, name_big_img),
                                    get_file(get_large_file(url_small_img)))


def main():
    create_work_dirs(path_file_in, folder_in, folder_out)
    urls_small_img = read_file(path_file_in)  # переменная для списка урлов с маленькими картинками
    number_proc = 10  # кол-во процессов
    with Pool(number_proc) as p:
        p.map(make_all, urls_small_img)
    print('DONE!')


if __name__ == '__main__':
    main()
