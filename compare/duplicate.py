import csv
from collections import Counter, defaultdict
import unicodedata

##with open('Customer_Pry_AddrInvalid.csv') as inputfile:
##    reader = csv.reader(inputfile)
##    inputm = list(reader)
####    inputm = ''.join(inputm)
##
####def Repeat(x): 
####    _size = len(x)
####    _word = len(word)
####    repeated = []  
####    for i in range(_size):
####        k = i + 1
####        for j in range(k, _size): 
####            if x[i] == x[j] and x[i] not in repeated: 
####                repeated.append(x[i])
####    return repeated
##done = 'Duplicate found '
##found ='NOT FOUND in masterlist'
##myList = inputm
##A = myList
##for x in set(map(tuple, A)):
##    j = ':'.join(x)
##    i = str(j)
##    h = i.isalnum()
##    if A.count(h)>0:
##        print()
##    
##    print('{} = {}'.format(h, A.count(x)))
##    if A.count(x)>1:
##        print ('{} = {}'.format(x, A.count(x)),'Duplicate(s) found')
##        print("\nProcess completed.")
##    
##f1_line=open('Customer_Pry_AddrInvalid.csv').readlines()
##Se = f1_line
##for x in Se:
##    j = ':'.join(x)
##    h = j.isalnum()
##    if Se.count(h)>0:
##        print ('{} = {}'.format(h, Se.count(x)),'Duplicate(s) found')
##print("\nProcess completed.")

d = (['ad',str(23), 'wa','le'])
e = ','.join(d)
f = e.strip(',')
if f.isalnum():
    print('true')
else:
    print('no')










