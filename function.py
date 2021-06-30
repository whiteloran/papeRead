import requests
from bs4 import BeautifulSoup
import re
import time
import csv
from concurrent.futures import ThreadPoolExecutor



def getarUrl(k):
    r1 = requests.get('https://proceedings.neurips.cc' + k)
    #print(r1.status_code)
    r = BeautifulSoup(r1.text, 'html.parser')
    return r

def getabstract(k,i):
    temp = []
    r = getarUrl(k.a.get('href'))
    oridata = r.find_all('p')
    theabstract =oridata[2].text
    thereviewlink1= r.find(name='div',attrs={'class':'col'})
    thereviewlink2 = thereviewlink1.find('div')
    for i in thereviewlink2.find_all('a'):
        temp.append(i.get('href'))
    themetareviewlink=temp[2]
    thereviewlink=temp[4]
    themetareview = getmetareview(themetareviewlink)
    thedata = [i,k.a.text,k.find('i').text,k.a.get('href'),theabstract,themetareview,thereviewlink]
    return thedata

def getmetareview(k):
    r = getarUrl(k)
    k = r.find('p').text
    return k


def writedb(therows):
    f = open('1.csv','w+',encoding='utf-8',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Num','Title','Author','Link','Abstract','MetaReview','ReviewLink'])
    csv_writer.writerows(therows)
    f.close()
