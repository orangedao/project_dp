#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

urls = [
    'https://apse2-uploads5.wikiart.org/images/salvador-dali.jpg!Portrait.jpg'
    'https://apse2-uploads7.wikiart.org/images/salvador-dali/un-chien-andalou-film-still-1928.jpg!PinterestLarge.jpg'
    'https://apse2-uploads1.wikiart.org/images/salvador-dali/the-great-masturbator-1929.jpg!PinterestLarge.jpg'
    'https://apse2-uploads5.wikiart.org/images/salvador-dali/the-persistence-of-memory-1931.jpg!PinterestLarge.jpg'
]


def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name(url):
	name = url.split('/')[-1]
	return name

def save_image(name, file_object):
	with open(name, 'bw') as f:
		for chunk in file_object.iter_content(8192):
			f.write(chunk)


def main():

	for url in urls:
		save_image(get_name(url), get_file(url))


if __name__ == '__main__':
    main()
