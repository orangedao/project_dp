#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# import re
import requests
# ------------------Обработка файлов в каталоге-------------
# -----------------Переменные------------

work_dir_in = 'files_in'
work_dir_out = 'files_out'
list_url_img = []  # список url img


# создаем рабочие дирректории
def create_work_dir():
    if not os.path.exists(work_dir_in):
        os.mkdir(work_dir_in)
        print('Рабочий каталог "%s" создан' % work_dir_in)
    if not os.path.exists(work_dir_out):
        os.mkdir(work_dir_out)
        print('Рабочий каталог "%s" создан' % work_dir_out)


# считываем исходные файлы
def read_work_files(work_dir_in):
    list_work_files = os.listdir(work_dir_in)
    for work_file in list_work_files:
        file_name = os.path.join(work_dir_in, work_file)
        f_in = open(file_name, 'r', encoding='utf-8')
        list_url_img = (f_in.readlines())
        f_in.close()
        # print(list_url_img)
    return list_url_img


# ф-я для поиска картинок по заданному шаблону
def save_img(read_work_files):
    for url in read_work_files:
        url_img = url.split(sep='!PinterestLarge.jpg')[0]
        # list_url_img = []
        list_url_img.append(url_img)

    count = 0
    for url in list_url_img:
        count += 1
        p = os.path.dirname(url)
        name_part1 = p.split(sep='/')[-1]
        name_part2 = os.path.basename(url)
        work_file_out = name_part1 + '-' + name_part2
        # print(work_file_out)
        file_name = os.path.join(work_dir_out, work_file_out)
        # downloading files
        print('downloading file # {count:03}-%s'.format(count=count) % name_part2)
        r = requests.get(url)
        with open(file_name, 'wb') as img:
            img.write(r.content)


def main():
    if not create_work_dir():
        save_img(read_work_files(work_dir_in))


if __name__ == '__main__':
    main()
