from tkinter import *
import os
import difflib

def compareFiles():
    return 0


root = Tk()

root.wm_title("Compare Gear")


# Created the first label here

enterFistFile = Label(root, text="Enter first file .txt, .csv, or xlx: ",fg="red")


# Inserted first label on the window
enterFistFile.grid(row=0,column=0)

# First entry text box creation and placment on window
enterFistFile = Entry(root)
enterFistFile.grid(row=1,column=0,pady=10, padx=5)

#Creating second label and placing it on the window
enterSecondFile = Label(root,text="Enter second file .txt, .csv, or xlx",fg="red")
enterSecondFile.grid(row=2,column=0)

# Creating post argugment entry box and placing it on the window/grid

enterSecondFile = Entry(root)
enterSecondFile.grid(row=3,column=0,pady=10, padx=5)

checkFiles = Button(root,text="Check", command=compareFiles)
checkFiles.grid(row=4,column=0,pady=10, padx=5)

def compareFiles():
    f1= enterFistFile.get()
    f2= enterSecondFile.get()
    f1_line=open(f1).readlines()  #open a file
    f2_line=open(f2).readlines() #open another file to compare
    differences = difflib.HtmlDiff().make_file(f1_line, f2_line, f1, f2) #check differences
    diff_report = open('index.html','w') #open as html file
    diff_report.write(differences) #save as html file
    print(differences)
    diff_report.close()

root.mainloop
