from tkinter import *


def testVulnerability():
    return 0
# Driver code
if __name__ == "__main__":
    root = Tk()

root.wm_title("First GUI Window")


# Created the first label here

enterURL = Label(root, text="Enter URL To test",fg="red")


# Inserted first label on the window
enterURL.grid(row=0,column=0)

# First entry text box creation and placment on window
enterText = Entry(root)
enterText.grid(row=1,column=0,pady=10, padx=100)

#Creating second label and placing it on the window
enterPostArg = Label(root,text="Enter post argument: ")
enterPostArg.grid(row=2,column=0)

# Creating post argugment entry box and placing it on the window/grid

enterPostArgText = Entry(root)
enterPostArgText.grid(row=3,column=0,pady=10, padx=100)

checkIfVunlerable = Button(root,text="Test", command=testVulnerability)
checkIfVunlerable.grid(row=4,column=0,pady=10, padx=100)

def testVulnerability():

    urlEntered = enterText.get()
    postArgEntered = enterPostArgText.get()

    value = checkIfVulnerable(urlEntered, postArgEntered)

    if value == 1:
        enterText.delete(0, END)
        enterText.insert(0,"Vulnerable")
    else:
        enterText.delete(0, END)
        enterText.insert(0, "Not vulnerable")
def checkIfVulnerable(url,postArg):

    # build the key value pair post argument to be send to the url

    data = {'userid': postArg}

    # lets prepare the post request

    result = requests.post(url,data)

    # now calculate if the responce time is greater than 1 second most probably application is vulnerable to sql injection

    if float(result.elapsed.total_seconds()) > 1:
        return 1
    else:
        return 0
root.mainloop()
