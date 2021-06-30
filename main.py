# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
from concurrent.futures import ThreadPoolExecutor


def task1(k):
    r1 = requests.get('https://proceedings.neurips.cc' + k)
    print(r.status_code)
    thedata = BeautifulSoup(r1.text, 'html.parser')
    return thedata


pool = ThreadPoolExecutor(10)
r = requests.get('https://proceedings.neurips.cc/paper/2020')
print(r.status_code)
origindata = BeautifulSoup(r.text, 'html.parser')
listdata = origindata.find_all('li')

print(listdata[3])

listsoup = []
name = []
author = []
linker = []
abstract = []
review = []
for i in range(3, len(listdata)):
    # thesoup=BeautifulSoup(listdata[i],'html.parser')
    # listsoup.append(thesoup)
    name.append(listdata[i].a.text)
    author.append(listdata[i].find('i').text)
    linker.append(listdata[i].a.get('href'))
    thedata = pool.submit(task1, listdata[i].a.get('href'))
    



#print(listsoup[1])
#k = listdata[3].find('i').text
#print(k)

p = listdata[3].a.text
print(p)

l = listdata[3].a.get('href')
print(l)
