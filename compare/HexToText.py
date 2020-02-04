
from tkinter import *
from tkinter import Tk
import os
import sys
import csv
##import dateparser
import io
##import xlrd
import unicodedata
import re
import mmap

reverse = {
'1100001':'A',
'1100010':'B',
'1100011':'C',
'1100100':'D',
'1100101':'E',
'1100110':'F',
'1100111':'G',
'1101000':'H',
'1101001':'I',
'1101010':'J',
'1101011':'K',
'1101100':'L',
'1101101':'M',
'1101110':'N',
'1101111':'O',
'1110000':'P',
'1110001':'Q',
'1110010':'R',
'1110011':'S',
'1110100':'T',
'0101000':'U',
'0100111':'V',
'0100110':'W',
'0100101':'X',
'1111001':'Y',
'1111010':'Z',
'1000001':'a',
'1000010':'b',
'1000011':'c',
'1000100':'d',
'1000101':'e',
'1000110':'f',
'1000111':'g',
'1001000':'h',
'1001001':'i',
'1001010':'j',
'1001011':'k',
'1001100':'l',
'1001101':'m',
'1001110':'n',
'1001111':'o',
'1010000':'p',
'1010001':'q',
'1010010':'r',
'1010011':'s',
'1010100':'t',
'0101110':'u',
'0101101':'v',
'0101100':'w',
'0101011':'x',
'0101010':'y',
'0101001':'z',
' ':' ',
'0111101':'!',
'0111100':'"',
'0111011':'#',
'0111010':'$',
'0111001':'%',
'0111000':'&',
'0110111':"'",
'0110110':'(',
'0110101':')',
'0110100':'*',
'0110011':'+',
'0110010':',',
'0110001':'-',
'0110000':'.',
'0101111':'/',
'|':'',
':':'0011110',
';':'0011101',
'<':'0011100',
'=':'0011011',
'>':'0011010',
'?':'0011001',
'@':'0011000',
}
print("Enter file path Eg: filelocate/file.txt: ")
inLoc = input (str("> "))
with open(inLoc, "r") as infilew:
    print("Enter decryption code: ")
    paswd = input("> ") 
    for word in infilew:
        s = word.find(paswd)
        count=0
        if s == -1:
            print('Password not match!')
        else:
            print('PASSWORD FOUND.')
            print("Enter Output file name: ")
            outLoc = input("> ")
            with io.open(inLoc, "r") as infile, open(outLoc, "w", encoding='utf-8') as outfile:
                for line in infile:
                    for src, target in reverse.items():
                        line = line.replace(src, target)
                    outfile.write(line)
            print('process completed sucessfully!')
            break

                                    


