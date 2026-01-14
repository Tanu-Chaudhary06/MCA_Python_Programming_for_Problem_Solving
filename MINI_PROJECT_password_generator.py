import random
import string
import tkinter as tk
from tkinter import messagebox

def generate():
    value = entry.get()

    if value.isdigit():
        length = int(value)

        if length >= 4:
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ""

            i = 0
            while i < length:
                password = password + random.choice(chars)
                i = i + 1

            messagebox.showinfo("Password", password)

        else:
            messagebox.showerror("Error", "Length must be 4 or more")

    else:
        messagebox.showerror("Error", "Please enter numbers only")

# GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")

label = tk.Label(window, text="Enter Password Length")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Generate Password", command=generate)
button.pack(pady=20)

window.mainloop()
