import tkinter as tk
from tkinter import messagebox, Text
from getpass import getpass
import pyAesCrypt
import os

def encrypt():
    name = name_entry.get()
    password = password_entry.get()
    buffersize = 512*1024
    try:
        pyAesCrypt.encryptFile(f"{name}.txt", f"{name}.aes", password, buffersize)
        os.remove(f"{name}.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def newuser():
    name = name_entry.get()
    password = password_entry.get()
    try:
        with open(f"{name}.txt", "w") as pf:
            pf.close()
        encrypt()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt():
    name = name_entry.get()
    password = password_entry.get()
    buffersize = 512*1024
    try:
        pyAesCrypt.decryptFile(f"{name}.aes", f"{name}.txt", password, buffersize)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def sign_up():
    newuser()
    messagebox.showinfo("Success", "User registered successfully!")

def log_in():
    decrypt()
    messagebox.showinfo("Success", "Logged in successfully!")
    # Display the contents of the decrypted file
    with open(f"{name_entry.get()}.txt", "r") as file:
        content = file.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, content)

def save_changes():
    name = name_entry.get()
    content = text_widget.get("1.0", tk.END)
    with open(f"{name}.txt", "w") as file:
        file.write(content)
    encrypt()
    messagebox.showinfo("Success", "Changes saved successfully!")

def log_out():
    text_widget.delete("1.0", tk.END)
    name = name_entry.get()
    if os.path.exists(f"{name}.txt"):
        with open(f"{name}.txt", "w") as file:
            file.write("")  # Clear the content of the file
root = tk.Tk()
root.title("User Registration and Login")

name_label = tk.Label(root, text="Username:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

signup_button = tk.Button(root, text="Sign Up", command=sign_up)
signup_button.pack()

login_button = tk.Button(root, text="Log In", command=log_in)
login_button.pack()

logout_button = tk.Button(root, text="Log Out", command=log_out)
logout_button.pack()

text_widget = Text(root, height=10, width=50)
text_widget.pack()

save_button = tk.Button(root, text="Save Changes", command=save_changes)
save_button.pack()

root.mainloop()