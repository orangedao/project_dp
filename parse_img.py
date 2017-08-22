# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

# urls = [
#     'https://uploads6.wikiart.org/images/salvador-dali/car-clothing-clothed-automobile.jpg!PinterestLarge.jpg',
#     'https://uploads4.wikiart.org/images/salvador-dali/costume-for-a-nude-with-a-codfish-tail.jpg!PinterestLarge.jpg',
#     'https://uploads4.wikiart.org/images/salvador-dali/design-for-set-curtain-for-labyrinth-i.jpg!PinterestLarge.jpg',
#     'https://uploads1.wikiart.org/images/salvador-dali/invisible-bust-of-voltaire.jpg!PinterestLarge.jpg'
# ]


folder_out = 'images'  # переменная каталога с картинками
folder_in = 'files_in'  # переменная каталога с входящими данными


# функция чтения файлов из каталога и получения списка ссылок
def read_file(folder_in):
    list_work_files = os.listdir(folder_in)
    for work_file in list_work_files:
        file_name = folder_in + '/' + work_file
        with open(file_name, 'r') as f_in:
            urls = f_in.readlines()
    # print(urls)
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


def main():
    urls = read_file(folder_in)
    for url in urls:
        save_image(get_name(url), get_file(get_large_file(url)))
    # read_file(folder_in)


if __name__ == '__main__':
    main()
