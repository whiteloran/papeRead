import requests
from bs4 import BeautifulSoup
import re
import time
import csv
from concurrent.futures import ThreadPoolExecutor
import pandas

def getarUrl(k):
    i=1
    while i<5:
        try:
            r1 = requests.get('https://proceedings.neurips.cc' + k)
            r = BeautifulSoup(r1.text, 'html.parser')
            return r    
        except requests.exceptions.ConnectionError:
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            time.sleep(3)
        except:
            time.sleep(3)       
        i += 1
    with open('config.txt','a+',encoding='utf-8') as f:
        f.write('https://proceedings.neurips.cc'+k)
        f.write('\n')
    text = []
    return text

def getabstract(k,i):
    j=i-1
    print(k.a.text)
    print('On going!')
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
    thereview = getreview(thereviewlink)
    thedata = [j,k.a.text,k.find('i').text,k.a.get('href'),theabstract,themetareview]
    tempreview = [z for line in thereview for z in line]
    for i in tempreview:
        thedata.append(i)
    #for i in range(1,len(thereview)):
        #for k in len(thereview[i]):
        #sac,st,wn,cn,cla,rtpw,rep,af = thereview[i]
    return thedata

def getmetareview(k):
    r = getarUrl(k)
    k = r.find('p').text
    return k

def getreview(k):
    p = []
    r = getarUrl(k)
    reviews = r.find_all('h3')
    for i in range(1,len(reviews)):
        sac,st,wn,cn,cla,rtpw,rep,af = getdetailreview(reviews[i])
        p.append([sac,st,wn,cn,cla,rtpw,rep,af])
    return p

def getdetailreview(k):
    sac = k.find_next_sibling('p')
    st = sac.find_next_sibling('p')
    wn = st.find_next_sibling('p')
    cn = wn.find_next_sibling('p')
    cla = cn.find_next_sibling('p')
    rtpw = cla.find_next_sibling('p')
    rep = rtpw.find_next_sibling('p')
    af = rep.find_next_sibling('p')
    return sac.text,st.text,wn.text,cn.text,cla.text,rtpw.text,rep.text,af.text

def writedbfirst():
    with open('sigmatrix.csv','a+',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Num','Title','Author','Link','Abstract','MetaReview','Review'])

def writedb(therows):
    with open('sigmatrix.csv','a+',encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(therows)


#def writexlsfirst():

#def writexls():


def addingdata(thefuturer):
    thedata = thefuturer.result()
    #print(thedata)
    writedb(thedata)
    print(thedata[0])
    print('Completed!')


def addingsoup(thedata):
    with open('site.html','w+',encoding='utf-8',newline='') as f:
        f.writelines(thedata)
