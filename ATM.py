username ='Murali krishna'
password ='Murali@123'

c_name = input("Enter your name: ")
c_pass = str(input("Enter your password: "))

if c_name==username and c_pass==password:
    print('''
    1.Deposit
    2.Withdraw
    3.mini_statement
    4.exit
      ''')
    Amount = 50000
    option=int(input("Enter your option: "))
    if option==1:
        dep=int(input("Enter your amount: "))
        Amount+=dep
        print("Your Total amount is:",Amount)
    elif option==2:
        withdraw=int(input("Enter the amount: "))
        Amount-=withdraw
        print("Your total amount: ",Amount)
    elif option==3:
        print("ATM MINI STATEMENT")
        print("Username: ",username)
        print("Your total amount: ",Amount)
        print("Thank you!")
    elif option==4:
        exit()
    else:
        print("please enter your credentials correctly")

