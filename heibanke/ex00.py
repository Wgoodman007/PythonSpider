#!/usr/bin/python

import requests
import re

Q1_ur1 = r'http://www.heibanke.com/lesson/crawler_ex00/'

ur1 = Q1_ur1
num_re = re.compiler(r'<h3>[^\d<]*?(\d+)[^\d<]*?</h3')
while True:
    print('reading web address',url)
    html = requests.get(url).text
    num = num_re.findall(html)
    if len(num) == 0:
        break
    else:
        url = Q1_ur1 + num[0]
print('end!')
