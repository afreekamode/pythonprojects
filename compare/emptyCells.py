
from tkinter import *
from tkinter import Tk
import os
import sys
import csv
import dateparser
import io
import xlrd
import unicodedata
import re
import string

print("Input file location: ")
inLoc = input("> ")
with open(inLoc, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    j = next(reader)
    for num, row, in enumerate(reader):
        if row[2] in (None, ''):
            print(num, j,'\n', row,'\n')
            
print('Done!')
##none = ''
##with open(inLoc, mode='r') as f:
##    reader = csv.reader(f)
##    for num, row in enumerate(reader):
##        if row[2] in (None, ''):
##            print (num, row, 'empty')

##with open(inLoc) as csvfile:
##
##    rest = []
##    with open(inloc, "rb") as f:
##        reader = csv.reader(f)
##        i = next(reader)
##        i=i[1:]
##        re=csv.DictReader(csvfile)
##        for row in re:
##            for x in i:
##                print (row[x])


