
                ###PROJECT TITLE HIRE PURCHASE PURSE #####

                      ###BY SIKIRU SHITTU #####
                      ### CODE LAGOS 3.0 #####

##Get User Profile

print('Welcome To "HPP" Hire Purchase Platform!')
print('You are User or Admin?')
ini = input()
if ini =='user':
     print('Please Signup Here')
     userFirst = input('Enter Your First Name >> ')
     userLast = input('Enter Your Last Name >> ')
     user_age = int(input('Enter Age >> '))
     difrr = 18 - user_age
     actual = difrr + user_age
     if user_age < 18:
         print('you most be at least 18 to apply')
         print('check back in ', difrr, 'years time when you are', actual, '!')
         rep = input('thank you!'.upper())
     else:
         user_phone = int(input('Enter Your Phone >> '))    
         user_email = input('Enter Your Email >> ')
         passwd = input('Enter Password >> ')
         print('Thank you,', userFirst.upper(), 'your registration is successful! your email is', user_email.upper(), 'and your password is ',passwd.upper() )
         passwdre = input('Enter Password to continue >> ')

##     userInfo = [userFirst, userLast, user_age, user_phone, user_email, ]
##     for info in userInfo:
##         if info == None:
##             print(info - 5)
##         else: 
##             print(info)
##elif ini == 'admin':
##    pwd= input('Loging Admin:create 4 letter password!-->')
##    print('Thank you, your password is >',pwd )
##    pwdre = input("Enter new password to continue \n")
##
##    ##Check User Password Validity
##    
##pos = 0
##while pwdre  != pwd and pos < len(pwd):
##    print("nope, this is not the password! Hint: letter ", end='')
##    print(pos +1, "is", pwd [pos] + ".",)
##    pwdre  = input("Try again: \n")
##    pos = pos + 1
##if pos == len(pwd) and pwd  != pwdre :
##    print("Too bad, you could'nt get it this time try again in 5min.")
##else:
##    print('Hello Admin, welcome!\n')
##    print('What did like to do ? pick a choice to continue...!',end='')
        
##Check User Password Validity
pos = 0
while passwdre  != passwd and pos < len(passwd ):
    print("nope, this is not the password! Hint: letter ", end='')
    print(pos +1, "is", passwd [pos] + ".",)
    passwdre = input("Try again: \n")
    pos = pos + 1
if pos == len(passwd) and passwd != passwdre :
    print("Too bad, you could'nt get it this time try again in 5min.")
else:
    print('Hello', userFirst.upper() ,'and welcome!\n')
    print('What would you like to do? pick a choice to continue...!')
    
## To show List Of available Operations
my_list = ['Enter A to: Evaluate', 'Enter B for: Monthly Repayment plan', 'Enter C: To get Balace\n\n',]
for i in my_list:
    if i == None:
       print(i - 5)
    else:
        print(i)
my_list2 = ['See Our Products Prices and Annum Interest Rate Bellow,\n use it to do your calculation we accept min of 4 year repayment tenure!', 'Car: $50000: Rate: 10%', 'Tricycle: $30000: Rate: 12%', 'Bicycle: $28000: Rate: 12%', 'Freezer: $5000: Rate: 15%']
for i in my_list2:
    if i == None:
       print(i - 5)
    else:
        print(i)
    
    def totop():
        print('select action')
    print('select action')
    choice = input('--> ')
    
## To Calculate Payment and repayment values

    if choice == 'a':
                x = amountFinanced = int(input('start calculating\nAmount Financed--> ',))
                y = termCharged = int(input('Term Charged%--> ',))
                z = tenure = int(input('Tenure--> ',))
                def interest(inter):
                    return x * y * 0.01 * z
                print('You will be paying --> ',interest(1) ,'per annum\n', end='',)
    elif choice == 'b':
                x = amountFinanced = int(input('start calculating\nAmount Financed--> ',))
                y = termCharged = int(input('Term Charged%--> ',))
                z = tenure = int(input('Tenure--> ',))
                i = x * y * 0.01 * z
                zmth = z * 12
                m = (x + i) / zmth
                print('You will be paying --> ',m, 'per month',end='')
    elif choice == 'c':
                x = amountFinanced = int(input('start calculating\nAmount Financed--> ',))
                y = termCharged = int(input('Term Charged%--> ',))
                z = tenure = int(input('Tenure'))
                amPaid = amountPaid = int(input('How much have you paid--> ',))
                i = x * y * 0.01 * z
                t = total = i + x
                bal = t - amPaid
                print('Your repayment balace is --> ',bal, end='')

    rep = ''
    name = 'yes'
    rep = input('Would you like to perform another action?! enter YES to continue NO to exit!\n>>')
    if rep == 'yes':
        print('Hello', userFirst.upper() ,'welcome back!\n')
        print('What would you like to do this time?  pick a choice to continue...!')
        if __name__ == "__main__": 
            totop()
    else:
        print('Thank you for doing business with us!')
        print('see you again')       

main()
