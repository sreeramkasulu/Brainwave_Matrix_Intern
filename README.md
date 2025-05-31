# 💳 ATM GUI System using Python

Welcome to the **ATM GUI Application**, a user-friendly and secure **Automated Teller Machine simulator** built with Python and Tkinter. This project simulates core ATM operations like **Login**, **User Registration**, **Check Balance**, **Deposit**, **Withdraw**, and **Logout**, storing user data securely in a local JSON file.

---

## 🎯 Project Objective

To build a functional GUI-based ATM system that:

- Allows users to securely **register** with a 4-digit PIN.
- Enables **login** authentication.
- Supports **balance inquiry**, **deposit**, **withdrawal**, and **logout** features.
- Persists user data using JSON file handling.

---

## 🧠 Features

- 🔐 **Secure Login System** using 4-digit PIN.
- 🧾 **User Registration** with validation.
- 💰 **Banking Operations**:
  - Check Balance
  - Deposit Money
  - Withdraw Money
- 💾 Data stored using JSON (`users.json` auto-created).
- 🖼️ GUI developed using **Tkinter** for a smooth user experience.
- 📂 Simple, readable code for beginners to learn Python GUI + File Handling.

---

## 📜 How It Works (Code Flow)

### 🔑 User Registration

```python
pin = simpledialog.askstring("Register", "Create a 4-digit PIN:")
self.users[pin] = {"balance": 0.0}
save_users(self.users)
```

- Validates PIN length.
- Initializes user balance to ₹0.0.
- Automatically creates and saves data to `users.json`.

---

### 🔐 Login System

```python
pin = simpledialog.askstring("Login", "Enter your 4-digit PIN:", show="*")
if pin in self.users:
    self.current_user = pin
    self.main_menu()
```

- Asks for PIN input.
- Verifies against stored user data.
- Grants access to the main ATM menu.

---

### 📊 Check Balance

```python
balance = self.users[self.current_user]["balance"]
messagebox.showinfo("Balance", f"Your balance is ₹{balance:.2f}")
```

- Displays current user balance.

---

### 💸 Deposit Money

```python
amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
if amount and amount > 0:
    self.users[self.current_user]["balance"] += amount
    save_users(self.users)
    messagebox.showinfo("Success", f"Deposited ₹{amount:.2f}")
```

---

### 💵 Withdraw Money

```python
amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
balance = self.users[self.current_user]["balance"]
if amount and 0 < amount <= balance:
    self.users[self.current_user]["balance"] -= amount
    save_users(self.users)
    messagebox.showinfo("Success", f"Withdrew ₹{amount:.2f}")
```

---

### 🚪 Logout

```python
self.current_user = None
self.create_login_screen()
```

---

## 📁 File Structure

```
ATM/
├── atm.py              # Main Python script (GUI logic)
├── users.json          # Auto-generated on first registration
├──atm-demo.mp4         # Demo video of project in action
└── README.md           # Project documentation
```

---

## 📹 Demo Video

🎬 **Project Walkthrough:**  
[▶️ Watch Demo on Google Drive](https://drive.google.com/file/d/1YaQprPwNGuS-O6fUemhGc-NoppzLpw58/view?usp=sharing)

---

## 🛠️ Requirements

- Python 3.x
- Tkinter (comes with Python)

---

## ▶️ How to Run

1. Ensure Python is installed.
2. Navigate to the project directory:

```bash
cd ATM
```

3. Run the app:

```bash
python atm.py
```

4. Use the GUI for:
   - New User Registration
   - Login
   - Balance Check
   - Deposit / Withdraw
   - Logout

---

## 👤 Author

**Sreeram Kasulu Penke**  
📧 sriramkasulu@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/sreeram-k-692996215) | [GitHub](https://github.com/sreeramkasulu)

---

> 🌟 *If you like this project, consider giving it a ⭐ and sharing with others!*
