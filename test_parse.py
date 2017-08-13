#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
# import urllib
# import urllib2


# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
url1 = 'https://uploads8.wikiart.org/images/philippe-halsman/garters-1939.jpg'
p = os.path.dirname(url1)
name_part1 = p.split(sep='/')[-1]
name_part2 = os.path.basename(url1)
file_name = name_part1 + '-' + name_part2
print(file_name)




# print("downloading with requests")
# r = requests.get(url1)
# # with open("code3.zip", "wb") as code:
# with open("001.jpg", "wb") as img:
#     img.write(r.content)
