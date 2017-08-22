# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

urls = [
    'https://uploads6.wikiart.org/images/salvador-dali/car-clothing-clothed-automobile.jpg!PinterestLarge.jpg',
    'https://uploads4.wikiart.org/images/salvador-dali/costume-for-a-nude-with-a-codfish-tail.jpg!PinterestLarge.jpg',
    'https://uploads4.wikiart.org/images/salvador-dali/design-for-set-curtain-for-labyrinth-i.jpg!PinterestLarge.jpg',
    'https://uploads1.wikiart.org/images/salvador-dali/invisible-bust-of-voltaire.jpg!PinterestLarge.jpg'
]

folder = 'images'


def get_large_file(url):
    url = url.split('!')[0]
    return url


def get_file(url):
    r = requests.get(url, stream=True)
    return r


def get_name(url):
    name = url.split('/')[-1].split('!')[-2]
    # folder = name.split('.')[0]

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.abspath(folder)
    print(name)

    return path + '/' + name


def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


def main():
    for url in urls:
        save_image(get_name(url), get_file(get_large_file(url)))


if __name__ == '__main__':
    main()
