import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "users.json"

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.root.geometry("350x300")
        self.users = load_users()
        self.current_user = None

        self.create_login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Welcome to the ATM", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Login", command=self.login_screen, width=20).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.register_screen, width=20).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    def login_screen(self):
        pin = simpledialog.askstring("Login", "Enter your 4-digit PIN:", show="*")
        if pin in self.users:
            self.current_user = pin
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def register_screen(self):
        pin = simpledialog.askstring("Register", "Create a 4-digit PIN:", show="*")
        if not pin or not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be 4 digits")
            return
        if pin in self.users:
            messagebox.showwarning("Warning", "PIN already exists")
            return
        self.users[pin] = {"balance": 0.0}
        save_users(self.users)
        messagebox.showinfo("Success", "Account created successfully")

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="ATM Main Menu", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Check Balance", command=self.check_balance, width=20).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit_money, width=20).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_money, width=20).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout, width=20).pack(pady=10)

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        messagebox.showinfo("Balance", f"Your balance is ₹{balance:.2f}")

    def deposit_money(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount and amount > 0:
            self.users[self.current_user]["balance"] += amount
            save_users(self.users)
            messagebox.showinfo("Success", f"Deposited ₹{amount:.2f}")
        else:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw_money(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        balance = self.users[self.current_user]["balance"]
        if amount and 0 < amount <= balance:
            self.users[self.current_user]["balance"] -= amount
            save_users(self.users)
            messagebox.showinfo("Success", f"Withdrew ₹{amount:.2f}")
        else:
            messagebox.showerror("Error", "Insufficient balance or invalid amount")

    def logout(self):
        self.current_user = None
        self.create_login_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
