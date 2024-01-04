import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self):
        self.balance = 1000  # initial balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ${amount}. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds"

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")

        self.atm = ATM()

        self.balance_label = tk.Label(root, text="Balance:")
        self.balance_label.grid(row=0, column=0)

        self.balance_display = tk.Label(root, text=self.atm.check_balance())
        self.balance_display.grid(row=0, column=1)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=1, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=4, column=0, columnspan=2, pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", self.atm.check_balance())

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            message = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", message)
            self.update_balance_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            message = self.atm.withdraw(amount)
            messagebox.showinfo("Withdraw", message)
            self.update_balance_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def update_balance_display(self):
        self.balance_display.config(text=self.atm.check_balance())

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()