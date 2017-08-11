#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
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


def main():
    create_work_dir()
    read_work_files(work_dir_in)
    # print(list_work_files)


if __name__ == '__main__':
    main()
