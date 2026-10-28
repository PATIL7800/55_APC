
import tkinter as tk
from tkinter import messagebox, ttk
import re


country_codes = {
    "India": "+91",
    "USA": "+1",
    "United Kingdom": "+44",
    "Canada": "+1",
    "Australia": "+61",
    "Japan": "+81",
    "Germany": "+49",
    "France": "+33",
    "UAE": "+971",
    "Nepal": "+977"
}


mobile_lengths = {
    "India": 10,
    "USA": 10,
    "United Kingdom": 10,
    "Canada": 10,
    "Australia": 9,
    "Japan": 10,
    "Germany": 10,
    "France": 9,
    "UAE": 9,
    "Nepal": 10
}


state_districts = {
    "Maharashtra": [
        "Kolhapur", "Pune", "Mumbai City", "Mumbai Suburban",
        "Sangli", "Satara", "Solapur", "Nashik", "Nagpur",
        "Thane", "Ratnagiri", "Sindhudurg", "Raigad", "Nanded"
    ],
    "Karnataka": [
        "Belagavi", "Bengaluru Urban", "Dharwad", "Mysuru", "Udupi"
    ],
    "Goa": ["North Goa", "South Goa"]
}


district_talukas = {
    "Kolhapur": [
        "Karveer", "Panhala", "Hatkanangale", "Shirol", "Kagal",
        "Gadhinglaj", "Chandgad", "Ajara", "Bhudargad",
        "Radhanagari", "Gaganbawada", "Shahuwadi"
    ],
    "Pune": [
        "Haveli", "Mulshi", "Maval", "Baramati", "Indapur",
        "Junnar", "Khed", "Ambegaon", "Daund", "Shirur",
        "Bhor", "Purandar"
    ],
    "Sangli": [
        "Miraj", "Tasgaon", "Palus", "Khanapur", "Jat",
        "Atpadi", "Walwa", "Shirala", "Kadegaon"
    ],
    "Satara": [
        "Satara", "Karad", "Wai", "Mahabaleshwar", "Phaltan",
        "Patan", "Koregaon", "Man"
    ],
    "Belagavi": [
        "Belagavi", "Khanapur", "Bailhongal",
        "Gokak", "Athani", "Chikkodi"
    ],
    "North Goa": ["Bardez", "Tiswadi", "Pernem"],
    "South Goa": ["Salcete", "Mormugao", "Quepem"]
}


def update_country_code(event=None):
    country_code.set(country_codes.get(country.get(), ""))


def update_districts(event=None):
    selected_state = state.get()
    district["values"] = state_districts.get(selected_state, [])
    district.set("")
    taluka["values"] = []
    taluka.set("")


# Update taluka list
def update_talukas(event=None):
    selected_district = district.get()
    taluka["values"] = district_talukas.get(selected_district, [])
    taluka.set("")



def register():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    mobile = entry_mobile.get().strip()
    address = entry_address.get("1.0", "end-1c").strip()
    password = entry_password.get()
    confirm_password = entry_confirm.get()

    selected_country = country.get()
    selected_state = state.get()
    selected_district = district.get()
    selected_taluka = taluka.get()

   
    required_fields = [
        (name, "Full Name", entry_name),
        (email, "Email", entry_email),
        (selected_country, "Country", country),
        (mobile, "Mobile Number", entry_mobile),
        (address, "Full Address", entry_address),
        (selected_state, "State", state),
        (selected_district, "District", district),
        (selected_taluka, "Taluka", taluka),
        (password, "Password", entry_password),
        (confirm_password, "Confirm Password", entry_confirm)
    ]

    for value, field_name, widget in required_fields:
        if not value:
            messagebox.showerror(
                "Validation Error",
                f"{field_name} is required!"
            )
            widget.focus_set()
            return

    if len(name) < 3:
        messagebox.showerror(
            "Validation Error",
            "Name must contain at least 3 characters!"
        )
        entry_name.focus_set()
        return

    if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", name):
        messagebox.showerror(
            "Validation Error",
            "Name can contain letters, spaces, dots, apostrophes and hyphens only!"
        )
        entry_name.focus_set()
        return

    
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(email_pattern, email):
        messagebox.showerror(
            "Validation Error",
            "Enter a valid email address, e.g. student@gmail.com!"
        )
        entry_email.focus_set()
        return

    # Country validation
    if selected_country not in country_codes:
        messagebox.showerror(
            "Validation Error",
            "Please select a valid country!"
        )
        country.focus_set()
        return

    # Mobile validation
    if not mobile.isdigit():
        messagebox.showerror(
            "Validation Error",
            "Mobile number must contain digits only!"
        )
        entry_mobile.focus_set()
        return

    expected_length = mobile_lengths[selected_country]

    if len(mobile) != expected_length:
        messagebox.showerror(
            "Validation Error",
            f"Mobile number must contain exactly "
            f"{expected_length} digits for {selected_country}!"
        )
        entry_mobile.focus_set()
        return

    if set(mobile) == {"0"}:
        messagebox.showerror(
            "Validation Error",
            "Mobile number cannot contain only zeros!"
        )
        entry_mobile.focus_set()
        return

    # Address validation
    if len(address) < 10:
        messagebox.showerror(
            "Validation Error",
            "Address must contain at least 10 characters!"
        )
        entry_address.focus_set()
        return

    # State validation
    if selected_state not in state_districts:
        messagebox.showerror(
            "Validation Error",
            "Please select a valid state!"
        )
        state.focus_set()
        return

    # District validation
    if selected_district not in state_districts[selected_state]:
        messagebox.showerror(
            "Validation Error",
            "Select a valid district for the selected state!"
        )
        district.focus_set()
        return

    # Taluka validation
    if selected_taluka not in district_talukas.get(
        selected_district, []
    ):
        messagebox.showerror(
            "Validation Error",
            "Select a valid taluka for the selected district!"
        )
        taluka.focus_set()
        return

    # Password length
    if len(password) < 8:
        messagebox.showerror(
            "Validation Error",
            "Password must contain at least 8 characters!"
        )
        entry_password.focus_set()
        return

    # Password strength
    if not re.search(r"[A-Z]", password):
        messagebox.showerror(
            "Validation Error",
            "Password must contain an uppercase letter!"
        )
        entry_password.focus_set()
        return

    if not re.search(r"[a-z]", password):
        messagebox.showerror(
            "Validation Error",
            "Password must contain a lowercase letter!"
        )
        entry_password.focus_set()
        return

    if not re.search(r"\d", password):
        messagebox.showerror(
            "Validation Error",
            "Password must contain a digit!"
        )
        entry_password.focus_set()
        return

    if not re.search(r"[^A-Za-z0-9]", password):
        messagebox.showerror(
            "Validation Error",
            "Password must contain a special character!"
        )
        entry_password.focus_set()
        return

    # Confirm password
    if password != confirm_password:
        messagebox.showerror(
            "Validation Error",
            "Passwords do not match!"
        )
        entry_confirm.focus_set()
        return

    # Successful registration
    messagebox.showinfo(
        "Success",
        "Registration Successful!\n\n"
        f"Full Name: {name}\n"
        f"Email: {email}\n"
        f"Mobile: {country_code.get()} {mobile}\n"
        f"Address: {address}\n"
        f"Country: {selected_country}\n"
        f"State: {selected_state}\n"
        f"District: {selected_district}\n"
        f"Taluka: {selected_taluka}"
    )


# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("450x800")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="Registration Form",
    font=("Arial", 18, "bold")
).pack(pady=10)


# Function to create entry fields
def add_entry(label_text, show=None):
    tk.Label(root, text=label_text).pack()
    entry = tk.Entry(root, width=35, show=show)
    entry.pack(pady=3)
    return entry



entry_name = add_entry("Full Name")


entry_email = add_entry("Email")


tk.Label(root, text="Country").pack()

country = ttk.Combobox(
    root,
    values=list(country_codes.keys()),
    state="readonly",
    width=32
)
country.pack(pady=3)
country.bind("<<ComboboxSelected>>", update_country_code)


tk.Label(root, text="Mobile Number").pack()

mobile_frame = tk.Frame(root)
mobile_frame.pack(pady=3)

country_code = tk.StringVar()

tk.Label(
    mobile_frame,
    textvariable=country_code,
    width=6,
    relief="sunken"
).pack(side="left", padx=4)

entry_mobile = tk.Entry(mobile_frame, width=27)
entry_mobile.pack(side="left")


tk.Label(root, text="Full Address").pack()

entry_address = tk.Text(
    root,
    width=33,
    height=3
)
entry_address.pack(pady=3)


tk.Label(root, text="State").pack()

state = ttk.Combobox(
    root,
    values=list(state_districts.keys()),
    state="readonly",
    width=32
)
state.pack(pady=3)
state.bind("<<ComboboxSelected>>", update_districts)


tk.Label(root, text="District").pack()

district = ttk.Combobox(
    root,
    state="readonly",
    width=32
)
district.pack(pady=3)
district.bind("<<ComboboxSelected>>", update_talukas)


tk.Label(root, text="Taluka").pack()

taluka = ttk.Combobox(
    root,
    state="readonly",
    width=32
)
taluka.pack(pady=3)


entry_password = add_entry("Password", show="*")


entry_confirm = add_entry("Confirm Password", show="*")

tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=12)


root.mainloop()
