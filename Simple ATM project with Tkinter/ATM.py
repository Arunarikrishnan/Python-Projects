import tkinter as tk
import random

class Bank:
    def __init__(self, name, account_number, balance, pin_number):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin_number = pin_number

    def account_detail(self):
        account_detail_window = tk.Toplevel(root)
        account_detail_window.title("Account Detail")
        account_detail_window.geometry("300x200")
        
        detail_label = tk.Label(account_detail_window, text="\n----------ACCOUNT DETAIL----------")
        detail_label.pack()
        name_label = tk.Label(account_detail_window, text=f"Account Holder: {self.name.upper()}")
        name_label.pack()
        acc_num_label = tk.Label(account_detail_window, text=f"Account Number: {self.account_number}")
        acc_num_label.pack()
        balance_label = tk.Label(account_detail_window, text=f"Available balance: Rs.{self.balance}")
        balance_label.pack()

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        deposit_status_label.config(text=f"Current account balance: Rs. {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            withdraw_status_label.config(text="Insufficient funds")
        else:
            self.balance = self.balance - self.amount
            withdraw_status_label.config(text=f"Rs. {self.amount} withdrawal successful!\nCurrent account balance: Rs. {self.balance}")

    def check_balance(self):
        balance_window = tk.Toplevel(root)
        balance_window.title("Check Balance")
        balance_window.geometry("200x100")
        balance_label = tk.Label(balance_window, text=f"Available balance: Rs. {self.balance}")
        balance_label.pack()

    def pin(self):  
        chances = 3
        while chances != 0:
            user_pin = int(pin_entry.get())
            if user_pin != self.pin_number:
                chances -= 1
                pin_status_label.config(text=f'Wrong pin number\nYou have {chances} chances left')
            else:
                transaction()

    def transaction(self):
        transaction_window = tk.Toplevel(root)
        transaction_window.title("Transaction")
        transaction_window.geometry("300x200")

        transaction_label = tk.Label(transaction_window, text="""
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
        transaction_label.pack()

        option_entry = tk.Entry(transaction_window)
        option_entry.pack()

        def execute_option():
            try:
                option = int(option_entry.get())
            except ValueError:
                option_status_label.config(text="Error: Enter 1, 2, 3, 4, or 5 only!")
                return

            if option == 1:
                account_detail()
            elif option == 2:
                check_balance()
            elif option == 3:
                deposit_amount = float(deposit_entry.get())
                deposit(deposit_amount)
            elif option == 4:
                withdraw_amount = float(withdraw_entry.get())
                withdraw(withdraw_amount)
            elif option == 5:
                transaction_window.destroy()
                create_receipt()

        execute_button = tk.Button(transaction_window, text="Execute", command=execute_option)
        execute_button.pack()

# Tkinter setup
root = tk.Tk()
root.title("ATM Simulator")

# Account Creation
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

balance_label = tk.Label(root, text="Enter initial balance (minimum 500):")
balance_label.pack()
balance_entry = tk.Entry(root)
balance_entry.pack()

pin_label = tk.Label(root, text="Enter a 4-digit PIN:")
pin_label.pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

def create_account():
    name = name_entry.get().capitalize()
    balance = float(balance_entry.get())
    pin_number = int(pin_entry.get())

    if balance >= 500 and len(pin_entry.get()) == 4:
        global atm
        atm = Bank(name, random.randint(11111, 99999), balance, pin_number)
        root.title(f"ATM Simulator - Welcome, {name}")
        create_account_button.config(state=tk.DISABLED)
        atm.pin()
    else:
        create_account_status.config(text="Invalid input. Balance must be at least 500, and PIN must be 4 digits.")

create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.pack()

create_account_status = tk.Label(root, text="")
create_account_status.pack()

# Deposit and Withdraw
deposit_label = tk.Label(root, text="Enter amount to deposit:")
deposit_label.pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()

withdraw_label = tk.Label(root, text="Enter amount to withdraw:")
withdraw_label.pack()
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()

deposit_button = tk.Button(root, text="Deposit", command=lambda: atm.deposit(float(deposit_entry.get())))
deposit_button.pack()

withdraw_button = tk.Button(root, text="Withdraw", command=lambda: atm.withdraw(float(withdraw_entry.get())))
withdraw_button.pack()

deposit_status_label = tk.Label(root, text="")
deposit_status_label.pack()

withdraw_status_label = tk.Label(root, text="")
withdraw_status_label.pack()

# PIN Status
pin_status_label = tk.Label(root, text="")
pin_status_label.pack()

root.mainloop()
