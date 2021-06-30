# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
from concurrent.futures import ThreadPoolExecutor
from function import *



lista=[]
def addingdata(thefuturer):
    global lista
    thedata = thefuturer.result()
    print(thedata)
    lista.append(thedata)
    return lista


pool = ThreadPoolExecutor(10)
r = requests.get('https://proceedings.neurips.cc/paper/2020')
print(r.status_code)
origindata = BeautifulSoup(r.text, 'html.parser')
listdata = origindata.find_all('li')


for i in range(2, len(listdata)):
    #print(listdata[i].a.text)
    lista = pool.submit(getabstract, listdata[i],i).add_done_callback(addingdata)


writedb(lista)

print('completed!')

print(lista[1])
