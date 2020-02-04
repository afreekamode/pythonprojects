global expression
#simple calculator assignment
##x = int(input('start calculating\n'))
##y = input()
##z = int(input())
##
##if y == '+':    
##    print('=',x + z)
##elif y == '*':
##    print('=',x * z)
##elif y == '-':
##    print('=',x - z)
##elif y == '/':
##    print('=',x / z)  
##else:
##    print('pls, enter valid value!')
##x = int(input())
##y = input()
##z = int(input())    
##if y == '+':    
##    print(x + z)
##elif y == '*':
##    print(x * z)
##elif y == '-':
##    print(x - z)
##elif y == '/':
##    print(x / z)
##else:
##    print('pls, enter valid value!')
expression = ""
my_list = ['A: Evaluate', 'B: Monthly Repayment', 'C: To Balace', 'E: Exit']
for i in my_list:
    if i == None:
       print(i - 5)
    else:
        print(i)
print('select choice')
##x = 0
##y = 0
##z = 0
##while True:
choice = input('--> ')
def irate(interest):
    return x * y * 0.01 * z
##i = interestCharged = x * y*0.01 * z
def zmth(perMonth):
    return z * 12
def m(monthlyRepayment):
    return (x + interest) / zmth
def t(total):
    return rate + x
##bal = t - amPaid
##zmth = z * 12
##m = monthlyRepayment = (x + i) / zmth
##t = total = i + x
##bal = t - amPaid


if choice == 'a':
    x = amountFinanced = int(input('start calculating\nAmount Financed-->',))
    y = termCharged = int(input('Term Charged%-->',))
    z = tenure = int(input('Tenure-->',))
    i = x * y * 0.01 * z
    print('=', i, end='',)
elif choice == 'b':
    x = amountFinanced = int(input('start calculating\nAmount Financed-->',))
    y = termCharged = int(input('Term Charged%-->',))
    z = tenure = int(input('Tenure-->',))
    i = x * y * 0.01 * z
    zmth = z * 12
    m = (x + i) / zmth
    print('=',m, end='')
elif choice == 'c':
    x = amountFinanced = int(input('start calculating\nAmount Financed-->',))
    y = termCharged = int(input('Term Charged%-->',))
    z = tenure = int(input('Tenure'))
    amPaid = amountPaid = int(input('Amount Paid-->',))
    i = x * y * 0.01 * z
    t = total = i + x
    bal = t - amPaid
    print('=',bal, end='')
elif choice == 'e':
    print(expression)  
else:
    print('pls, enter valid value!')
x = int(input())
y = input()
z = int(input())    
if y == '+':    
    print(x + z)
elif y == '*':
    print(x * z)
elif y == '-':
    print(x - z)
elif y == '/':
    print(x / z)
else:
    print('pls, enter valid value!')

def clear():
    global expression
    expression = "e"
    equation.set("")
choice = input()





