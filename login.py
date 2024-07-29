import tkinter as tk
from tkinter import messagebox

def load_users():
    try:
        with open("users.txt", "r") as file:
            users = {}
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
        return users
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

users = load_users()

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username in users and users[username] == password:
        root.destroy()
        start_tetris()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    reg_window = tk.Toplevel(root)
    reg_window.title("Register")

    tk.Label(reg_window, text="New Username").pack()
    reg_entry_username = tk.Entry(reg_window)
    reg_entry_username.pack()

    tk.Label(reg_window, text="New Password").pack()
    reg_entry_password = tk.Entry(reg_window, show="*")
    reg_entry_password.pack()

    def save_credentials():
        new_username = reg_entry_username.get()
        new_password = reg_entry_password.get()
        if new_username in users:
            messagebox.showerror("Error", "Username already exists")
        else:
            users[new_username] = new_password
            save_users(users)
            messagebox.showinfo("Success", "Registration Successful")
            reg_entry_username.delete(0, tk.END)  
            reg_entry_password.delete(0, tk.END)

    tk.Button(reg_window, text="Register", command=save_credentials).pack()

def start_tetris():

    messagebox.showinfo("Login Successful", "Starting Tetris game...")

root = tk.Tk()
root.title("Tetris Login")
root.geometry("400x300") 

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack()
tk.Button(root, text="Register", command=register).pack()

root.mainloop()
