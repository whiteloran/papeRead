# -*- coding:utf-8 -*-
from sys import winver
import requests
from bs4 import BeautifulSoup
import re
import os
import time
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED

from requests import exceptions
from function import *

def getcontext():
    pool = ThreadPoolExecutor(10)
    while True:
        try:
            r = requests.get('https://proceedings.neurips.cc/paper/2020')
            print(r.status_code)
            break
        except:
            time.sleep(5)

    print('Connected!')

    if os.path.exists('site.html') == False:
        addingsoup(r.text)

    origindata = BeautifulSoup(r.text, 'html.parser')


    listdata = origindata.find_all('li')

    writedbfirst()

    all_task =[pool.submit(getabstract, listdata[i], i).add_done_callback(addingdata) for i in range(2,len(listdata))]

    pool.shutdown(wait=True)
    print('Final completed!')

if __name__ == "__main__":
    getcontext()

