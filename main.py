# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
from concurrent.futures import ThreadPoolExecutor
from function import *



lista=[]

pool = ThreadPoolExecutor(10)
r = requests.get('https://proceedings.neurips.cc/paper/2020')
print(r.status_code)
origindata = BeautifulSoup(r.text, 'html.parser')
listdata = origindata.find_all('li')


for i in range(2, len(listdata)):
    #print(listdata[i].a.text)
    pool.submit(getabstract, listdata[i],i).add_done_callback(addingdata)

#print(listedata)
writedb(lista)

print('completed!')

print(lista[1])

#print(listdata[3])

#listedata = []
#name = []
#author = []
#linker = []
#abstract = []
#review = []
#metareview = []