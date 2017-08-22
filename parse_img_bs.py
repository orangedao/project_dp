# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import requests
from bs4 import BeautifulSoup

# urls = [
#     'https://d32dm0rphc51dk.cloudfront.net/Rn549IGXSwy20o5rK2FWrw/larger.jpg'
# ]


folder = 'images'


def get_html(url):
    # r = requests.get(url)
    # return r.text

    with open(url, 'r') as f:
        # f.read()
        return f.read()


def get_title(html):
    parser1 = 'html.parser'
    parser2 = 'html.parser'

    soup = BeautifulSoup(html, parser2)

    artist_name = soup.find('span', class_='artist-name').text.split(':')[0]
    artist_list = soup.find('span', class_='artist-list')

    title = artist_name

    return title


def main():
    url = 'Dali_classic.html'
    print(get_title(get_html(url)))
    # print(get_html(url))


if __name__ == '__main__':
    main()
