
from tkinter import *
from tkinter import Tk
import os
import sys
import csv
import io
import pandas as pd 

g = "Date, Day, Temperature, Rainfall, Flyers, Price, Sales"
print("Input file location: ")
inLoc = input("> ")
  
# making data frame from csv file 
nba = pd.read_csv(inLoc)
  
# replacing na values with 'Empty' 
nba.fillna("EMPTY", inplace = True) 

print(nba.head(),'\n')
nba.to_csv()

# filter rows for 'empty' using the boolean expression
nba_empty = nba['Day']=='EMPTY'
nba_empty = nba[nba_empty]
print('FILLTERED ROWS WITH EMPTY CELLS ONLY:\n\n', nba_empty)
nba_empty.to_csv('rowEm1.csv')

print('Done!')
