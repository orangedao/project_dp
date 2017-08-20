#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

urls = [
    'https://d32dm0rphc51dk.cloudfront.net/Rn549IGXSwy20o5rK2FWrw/larger.jpg'
    ]

def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name(url):    	    
    name = url.split('/')[-1]
    folder = name.split('.')[0]

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    path = os.path.abspath(folder)

    return path + '/' + name


def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


def main():

    for url in urls:
        save_image(get_name(url), get_file(url))


if __name__ == '__main__':
    main()
