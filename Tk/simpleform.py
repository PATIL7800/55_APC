
import tkinter as tk
from tkinter import messagebox
import re

# Register function
def register():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get()
    confirm_password = entry_confirm.get()

    # Check empty fields
    if not name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate name
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain letters only!")
        return

    # Validate email
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showerror("Error", "Enter a valid email address!")
        return

    # Validate password
    if len(password) < 6:
        messagebox.showerror(
            "Error", "Password must contain at least 6 characters!"
        )
        return

    # Confirm password
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Success message
    messagebox.showinfo(
        "Success",
        f"Registration Successful!\n\n"
        f"Name: {name}\n"
        f"Email: {email}"
    )


# Create window
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x350")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Registration Form",
    font=("Arial", 18, "bold")
).pack(pady=15)

# Name
tk.Label(root, text="Full Name").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Email
tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

# Confirm Password
tk.Label(root, text="Confirm Password").pack()
entry_confirm = tk.Entry(root, width=30, show="*")
entry_confirm.pack(pady=5)

# Register button
tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    width=15
).pack(pady=15)

# Run application
root.mainloop()
