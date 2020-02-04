
# FMN PLC INVENTORY MONITOR APP
open_stock = 1000
stock_balance = 15000
sales = 0
stock_balance = open_stock - sales
open_stock = open_stock
pdk1 = 0
pdk2 = 0
pdk3 = 0
pdk4 = 0
pdk5 = 0
pdk6 = 0
pdk7 = 0
pdk_total = pdk1 + pdk2 + pdk3 + pdk4 + pdk5 + pdk6 + pdk7
option = 0
deposite = 0
chances = 0
 
import sys

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
print(":::::::::::::::::::::::::::::::::::WELCOME::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::::::::FMN PLC INVENTORY MONITOR APP::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

 
def inve_oper():
    answer = input("Would you like to make another transaction y/n?: ").lower()
    if answer == 'y':
        active = True
    else:
        active = False
        sys.exit("Thank you for using our App")
 
active = True

while chances < 3:
    pwd = int(input("\nWelcome, Please Enter Your Password: "))
    if pwd == (1234):
        print("\nHello Mr.B, choose the action you want to perform\n")
   
        while active:
            print("1: New Stock")
            print("2: Sale")
            print("3: To Check Stock Balance")
            print("4: Fund transfer")
            print("5: Change password")
            print("6: Quit")
 
            option = int(input("\nEnter an Option: "))
 
            if option == 1:
                open_stock = int(input("How much would you like to add: "))
                print("\nYour stock has been updated with " + str(open_stock)+ "Bags.\nAnd Your Sotck Balance is " + str(stock_balance + open_stock)+ "Bags")
                answer = input("\nWould you like to perform another action? if YES! press 'y' to return to the main menu. Else press 'n' to Quit: ").lower()
                if answer == 'y':
                    active = True
                else:
                    print("\nGoodbye")
                    active = False
                    sys.exit("Thank you for using our App") 
                    stock_balance = open_stock - sales
                    break
            
            elif option == 2:
                print("Your Stock Balance is:" + str(stock_balance))
                sales = int(input("\nEnter stock differeces:"))
                if sales > stock_balance:
                    print("\nRequest is out of range, Please, order for more stock then try again")
                    stock_balance = open_stock - sales
                else:
                    print("\nDebit Alert:\nYour stock has been updated with the differebces of" + str(sales)+"Bags\nAnd current stock is " + str(stock_balance - sales)+"Bags")
                    answer = input("\nWould you like to perform another action? if YES! press 'y' to return to the main menu. Else press 'n' to Quit: ").lower()
                    if answer == 'y':
                        active = True
                    else:
                        print("\nTake Your Card")
                        active = False
                        sys.exit("Thank you for using our App")
                        break
                        
            elif option == 3:
                print("Your available balance is: NGN" + str(main_balance))
                answer = input("\nWould you like to perform another transaction? if YES! press 'y' to return to the main menu. Else press 'n' to Quick: ").lower()
                if answer == 'y':
                    active = True
                else:
                    print("\nTake Your Card")
                    active = False
                    sys.exit("Thank you for using Codelagos Bank ATM")


            elif option == 4:
                fund_transfer = int(input("How much would you like to transfer: NGN"))
                if fund_transfer < balance:
                    print("Transaction successfully!\nAlert charge NGN" + str(alert_charge)+"\nAnd current balance is NGN"+ str(main_balance - fund_transfer - alert_charge))
                    answer = input("\nWould you like to perform another transaction? if YES! press 'y' to return to the main menu. Else press 'n' to Quick: ").lower()
                    if answer == 'y':
                        active = True
                else:
                    print("Insuffient fund!")
                    answer = input("\nWould you like to perform another transaction? if YES! press 'y' to return to the main menu. Else press 'n' to Quick: ").lower()
                    active = False
                    sys.exit
                    break

            elif option == 5:
                change_pin = int(input("Enter your new pin here: "))
                if change_pin > 0:
                    print("Your pin has been changed successfully, Thank you for using this service")
                    answer = input("\nWould you like to perform another transaction? if YES! press 'y' to return to the main menu. Else press 'n' to Quick: ").lower()
                    if answer == 'y':
                        active = True
                else:
                    print("Enter valid pin to proceed")
                    answer = input("\nWould you like to perform another transaction? if YES! press 'y' to return to the main menu. Else press 'n' to Quick: ").lower()
                    active = False
                    sys.exit
                    break    
                    
            elif option == 6:
                print("Locking your device...\n")
                print("Thank you for using this service")
                sys.exit("Thank you for using this service")
            
    elif pin != ("1234"):
        print("Invalid Pin")
        chances = chances +1
        if chances == 3:
            print("\nACOUNT BLOCKED! ")
            break
