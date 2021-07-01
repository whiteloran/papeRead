#import gensim
import scipy
import numpy
import re
import pandas
#import csv


#with open('./sigmatrix3','r',encoding='utf-8') as f:
    #oridata = f.readlines()


#print(oridata[5])

data = pandas.read_excel('./db/sigmatrix3.xlsx',header=0)
data = data.values
oridata = data[:][0:38]

print(oridata[0])