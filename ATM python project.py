#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
class bank():
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Rs.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Rs.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: Rs.", self.balance)
        print()
        
    def pin(self):  
        chances=3
        while chances!=0:
            user_pin=int(input('Enter your pin:'))
            if user_pin!=pin_number:
                chances-=1
                print('Wrong pin number')
                print(f'you have {chances} chances left')
                
            else:
                atm.transaction()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rs.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rs.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
               
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Rs.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    break
                 
 
print("*******WELCOME TO BANK *******")
print("________________________________\n")
print("----------ACCOUNT CREATION----------")
while True:
    name=input('Enter your name:').capitalize()#+' '+input('Enter your last name:').capitalize()
    if name.isalpha():
        print(name)
        break
    else:
        print('Enter alpha only')
#name = input("Enter your name: ")
account_number=random.randint(11111,99999)
#account_number = input("Enter your account number: ")
while True:
        balance=int(input('Please input a value to deposit to start an account:'))
        if balance >= 500:
            if balance%100==0:
                print('Your opening balance is',balance)
                break
            else:
                print('Enter Multiple of 100 only')
        else:
            print('Enter minimum 500 only')
#print("Congratulations! Account created successfully......\n")
 
atm = bank(name, account_number,balance)

while True:
    try:
        pin_number=int(input('Please input a 4 digit pin of your choice:'))
        if len(str(pin_number)) == 4:
            print("Congratulations! Account created successfully......\n")
            break
        if len(str(pin_number)) > 4 or len(str(pin_number)) <5:
            print('Please enter 4 digits only')
    except ValueError:
        print('please enter digits only')

atm.pin()
 
'''while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("Thanks for choosing us as your bank \n Visit us again!")
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")'''


# In[ ]:





# In[ ]:




