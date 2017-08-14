#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import requests
from datetime import datetime, date, time

now = datetime.now()
my_day = now.strftime("%d")
my_month = now.strftime("%m")
my_year = now.strftime("%Y")
my_hour = now.strftime("%H")
my_minute = now.strftime("%M")
my_second = now.strftime("%S")
my_date = '%s-%s-%s' % (my_year, my_month, my_day)
my_time = '%s-%s-%s' % (my_hour, my_minute, my_second)

# ------------------Обработка файлов в каталоге-------------
# -----------------Переменные------------

work_dir_in = 'files_in'
work_dir_out = 'files_out'
list_html_markup = []  # список html разметки


# создаем рабочие дирректории
def create_work_dir():
    if not os.path.exists(work_dir_in):
        os.mkdir(work_dir_in)
        print('Рабочий каталог "%s" создан' % work_dir_in)
    if not os.path.exists(work_dir_out):
        os.mkdir(work_dir_out)
        print('Рабочий каталог "%s" создан' % work_dir_out)


# считываем исходные файлы и добавляем html разметку в список
def read_work_files(work_dir_in):
    list_work_files = os.listdir(work_dir_in)
    for work_file in list_work_files:
        file_name = os.path.join(work_dir_in, work_file)
        f_in = open(file_name, 'r', encoding='utf-8')
        list_html_markup.append(f_in.read())
        f_in.close()
    # print(len(list_html_markup))


# ф-я для поиска картинок по заданному шаблону
def find_all_img():
    pattern = r'https://uploads[0-9]\.wikiart\.org/images/[a-zA-Z0-9_\-\/]+\.jpg'
    for html_markup in list_html_markup:
        # создаем список картинок
        list_img_link = (re.findall(pattern, str(html_markup)))
        # print(list_img_link[:5])
        count = 0

        for url in list_img_link:
            count += 1
            p = os.path.dirname(url)
            name_part1 = p.split(sep='/')[-1]
            name_part2 = os.path.basename(url)
            file_name = name_part1 + '-' + name_part2
            # downloading files
            print('downloading file # {count:03}-%s'.format(count=count) % name_part2)
            r = requests.get(url)
            with open('files_out/%s.jpg' % file_name, 'wb') as img:
                img.write(r.content)


def main():
    create_work_dir()
    read_work_files(work_dir_in)
    find_all_img()
    # save_img()
    # get_images()

    # print(list_work_files)


if __name__ == '__main__':
    main()
