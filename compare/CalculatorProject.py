# import everything from tkinter module
from tkinter import *
# globally declare the expression variable
expression = ""
 
# Function to update expression in the text entry box
def press(alph):
    # point out the global expression variable
    global expression
    
    # concatenation of string
    expression += str(alph)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluates the expression and str function convert the result into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialze the expression variable by empty string
        expression = ""
 
    # if error is generated then handle by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light grey")
 
    # set the title of GUI window
    gui.title("Calculator")
 
    # set the configuration of GUI window
    gui.geometry("650x260")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=100, ipady=8)
 
    equation.set('0')
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                     command=lambda: press(1), height=2, width=5)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='white',
                     command=lambda: press(2), height=2, width=5)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='white',
                     command=lambda: press(3), height=2, width=5)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='white',
                     command=lambda: press(4), height=2, width=5)
    button4.grid(row=2, column=3)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='white',
                     command=lambda: press(5), height=2, width=5)
    button5.grid(row=2, column=4)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='white',
                     command=lambda: press(6), height=2, width=5)
    button6.grid(row=2, column=5)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=2, width=5)
    button7.grid(row=2, column=6)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=2, width=5)
    button8.grid(row=2, column=7)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                     command=lambda: press(9), height=2, width=5)
    button9.grid(row=2, column=8)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                     command=lambda: press(0), height=2, width=5)
    button0.grid(row=2, column=9)
##    cfreatin alphabets
    button1 = Button(gui, text=' A ', fg='black', bg='white',
                     command=lambda: press(A), height=2, width=5)
    button1.grid(row=3, column=0)
 
    button2 = Button(gui, text=' B ', fg='black', bg='white',
                     command=lambda: press(B), height=2, width=5)
    button2.grid(row=3, column=1)
 
    button3 = Button(gui, text=' C ', fg='black', bg='white',
                     command=lambda: press(C), height=2, width=5)
    button3.grid(row=3, column=2)
 
    button4 = Button(gui, text=' D ', fg='black', bg='white',
                     command=lambda: press(D), height=2, width=5)
    button4.grid(row=3, column=3)
 
    button5 = Button(gui, text=' E ', fg='black', bg='white',
                     command=lambda: press(E), height=2, width=5)
    button5.grid(row=3, column=4)
 
    button6 = Button(gui, text=' F ', fg='black', bg='white',
                     command=lambda: press(F), height=2, width=5)
    button6.grid(row=3, column=5)
 
    button7 = Button(gui, text=' G ', fg='black', bg='white',
                     command=lambda: press(H), height=2, width=5)
    button7.grid(row=3, column=6)
 
    button8 = Button(gui, text=' H ', fg='black', bg='white',
                     command=lambda: press(H), height=2, width=5)
    button8.grid(row=3, column=7)
 
    button9 = Button(gui, text=' I ', fg='black', bg='white',
                     command=lambda: press(I), height=2, width=5)
    button9.grid(row=3, column=8)

    button9 = Button(gui, text=' J ', fg='black', bg='white',
                     command=lambda: press(J), height=2, width=5)
    button9.grid(row=3, column=9)

    button1 = Button(gui, text=' K ', fg='black', bg='white',
                     command=lambda: press(K), height=2, width=5)
    button1.grid(row=4, column=0)
 
    button2 = Button(gui, text=' L ', fg='black', bg='white',
                     command=lambda: press(L), height=2, width=5)
    button2.grid(row=4, column=1)
 
    button3 = Button(gui, text=' M ', fg='black', bg='white',
                     command=lambda: press(M), height=2, width=5)
    button3.grid(row=4, column=2)
 
    button4 = Button(gui, text=' N ', fg='black', bg='white',
                     command=lambda: press(N), height=2, width=5)
    button4.grid(row=4, column=3)
 
    button5 = Button(gui, text=' O ', fg='black', bg='white',
                     command=lambda: press(O), height=2, width=5)
    button5.grid(row=4, column=4)
 
    button6 = Button(gui, text=' P ', fg='black', bg='white',
                     command=lambda: press(P), height=2, width=5)
    button6.grid(row=4, column=5)
 
    button7 = Button(gui, text=' Q ', fg='black', bg='white',
                     command=lambda: press(Q), height=2, width=5)
    button7.grid(row=4, column=6)
 
    button8 = Button(gui, text=' R ', fg='black', bg='white',
                     command=lambda: press(R), height=2, width=5)
    button8.grid(row=4, column=7)
 
    button9 = Button(gui, text=' S ', fg='black', bg='white',
                     command=lambda: press(S), height=2, width=5)
    button9.grid(row=4, column=8)

    button9 = Button(gui, text=' T ', fg='black', bg='white',
                     command=lambda: press(T), height=2, width=5)
    button9.grid(row=4, column=9)

    button1 = Button(gui, text='U', fg='black', bg='white',
                     command=lambda: press(U), height=2, width=5)
    button1.grid(row=5, column=0)
 
    button2 = Button(gui, text='V', fg='black', bg='white',
                     command=lambda: press(V), height=2, width=5)
    button2.grid(row=5, column=1)
 
    button3 = Button(gui, text='W', fg='black', bg='white',
                     command=lambda: press(W), height=2, width=5)
    button3.grid(row=5, column=2)
 
    button4 = Button(gui, text='X', fg='black', bg='white',
                     command=lambda: press(X), height=2, width=5)
    button4.grid(row=5, column=3)
 
    button5 = Button(gui, text='Y', fg='black', bg='white',
                     command=lambda: press(Y), height=2, width=5)
    button5.grid(row=5, column=4)
 
    button6 = Button(gui, text='Z', fg='black', bg='white',
                     command=lambda: press(Z), height=2, width=5)
    button6.grid(row=5, column=5)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=2, width=5)
    button7.grid(row=5, column=6)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=2, width=5)
    button8.grid(row=5, column=7)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                     command=lambda: press(9), height=2, width=5)
    button9.grid(row=5, column=8)

    button9 = Button(gui, text=' 0 ', fg='black', bg='white',
                     command=lambda: press(0), height=2, width=5)
    button9.grid(row=5, column=9)
    
    clear = Button(gui, text='CLEAR', fg='white', bg='red',
                   command=clear, height=3, width=15)
    clear.grid(row=6, column='1')
 
    # start the GUI
    gui.mainloop()
