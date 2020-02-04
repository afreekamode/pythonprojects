
from tkinter import *
from tkinter import Tk
import os
import sys
import difflib
import csv
import dateparser
import io
import xlrd
import unicodedata
import re

def write(string):
    text_box.config(state=NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=DISABLED)
    
##workbook = xlrd.open_workbook('my_file_name.xls')    
def convert():
    cov = enterCovFile.get()
    convtz = convtout.get()
    # open the output csv
    with open(convtz, 'w', encoding="utf-8") as myFile:

    # define a writer
        wr = csv.writer(myFile, delimiter="\t")
    # open the xlsx file 
        myfile = xlrd.open_workbook(cov,'r')
    # get a sheet
        mysheet = myfile.sheet_by_index(0)
        co = mysheet
        write("In progress....")

    # write the rows
        for colnum in range(co.ncols):
            encode = wr.writerow(co.row_values(colnum))
            st = str(mysheet.row_values(colnum))
            match = re.search(r'^\d\d\d\d/(0?[1-9]|1[0-2])/(0?[0-9][43390.0])/(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$', convtz)
        write("File converted successfully, your " + convtz + " file is ready. \n\n. Thanks for using comApp")
        print(st)
        
def compareFiles():
    return 0

def compareFiles():
    f1 = enterFirstFile.get()
    f2 = enterSecondFile.get()
    reportz = output.get()
    report = reportz + '.html'

##f1='Lemonade1.csv'
##f2='Lemonade2.csv'
    f1_line=open(f1).readlines()  #open a file
    f2_line=open(f2).readlines() #open another file to compare
    differences = difflib.HtmlDiff().make_file(f1_line, f2_line, f1, f2) #check differences
    diff_report = open(report,'w') #open as html file
    file = diff_report.write(differences) #save as html file
    write("Files comparing completed successfully, your " + report + " file is ready. \n\nSteps to view the report:\n\n1. Right click on the HTML file \n2. Select open with, then \n3. Select your favorite browser to view the report.")
    
if __name__ == "__main__":
    root = Tk()

 # set the background colour of GUI window
root.configure(background="green")

##image = PhotoImage(file='FMN.ico')
##imgLabel = Label(root, image=image)
##
##imgLabel.grid(row=1,column=0, padx=20, sticky='w')

    # set the title of GUI window
root.wm_title("Files Compare App")

 
    # set the configuration of GUI window
root.geometry("950x780")

# Created the first label here

enterFirstFile = Label(root, text="Enter first file .txt, .csv, or xlx: ",fg="white",background="green")

# Inserted first label on the window
enterFirstFile.grid(row=1,column=0, pady=5)

# First entry text box creation and placment on window
enterFirstFile = Entry(root)
enterFirstFile.grid(row=2,column=0, padx=5)


#Creating second label and placing it on the window
enterSecondFile = Label(root,text="Enter second file .txt, .csv, or xlx",fg="white", background="green")
enterSecondFile.grid(row=3,column=0, pady=5)

# Creating post argugment entry box and placing it on the window/grid

enterSecondFile = Entry(root)
enterSecondFile.grid(row=4,column=0, pady=5, padx=5,)



#Creating convert label and placing it on the window
enterCovFile = Label(root,text="Here, you can convert your file other than \n(csv or text) file to .txt or .csv file:",fg="yellow", background="green")
enterCovFile.grid(row=2,column=1, pady=5)

# Creating convert entry box and placing it on the window/grid

enterCovFile = Entry(root)
enterCovFile.grid(row=3,column=1, pady=5, padx=5,)

#Creating output label and placing it on the window
output = Label(root,text="Enter output name (example: fileName.):",fg="white", background="green")
output.grid(row=5,column=0)

# Creating post argugment entry box and placing it on the window/grid

output = Entry(root)
output.grid(row=6,column=0, pady=5, padx=5,)

#Creating convtout label and placing it on the window
convtout = Label(root,text="Enter convt name (example: fileName.):",fg="white", background="green")
convtout.grid(row=4,column=1)

# Creating post argugment entry box and placing it on the window/grid

convtout = Entry(root)
convtout.grid(row=5,column=1, pady=5, padx=5,)

    
checkFiles = Button(root,text="Run", command=compareFiles)
checkFiles.grid(row=7,column=0, pady=5, padx=50)

ext = Button(root, text='Exit',fg='white', bg='red', command=root.destroy)
ext.grid(row=8,column=1, padx=50 )

# Creating conv button box and placing it on the window/grid
convert = Button(root, text='Convert',fg='white', bg='red', command=convert)
convert.grid(row=6,column=1, pady=5, padx=5, )

text_box = Text(root, state=DISABLED)
text_box.grid(row=8, column=0, pady=5, padx=30)

copyrit = Label(root, text="(C)2018 FMN PLC:\n Developed by BA. IT Audit ",fg="green")


# Inserted first label on the window
copyrit.grid(row=9,column=0)
root.mainloop()
