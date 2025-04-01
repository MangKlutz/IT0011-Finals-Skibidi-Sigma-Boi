import tkinter as tk
from tkinter import messagebox
from src.models.user import User
from src.utils.db_handler import add_user_to_db

class SignupForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up Form")

        self.first_name_label = tk.Label(master, text="First Name")
        self.first_name_label.pack()
        self.first_name_entry = tk.Entry(master)
        self.first_name_entry.pack()

        self.middle_name_label = tk.Label(master, text="Middle Name")
        self.middle_name_label.pack()
        self.middle_name_entry = tk.Entry(master)
        self.middle_name_entry.pack()

        self.last_name_label = tk.Label(master, text="Last Name")
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.pack()

        self.birthday_label = tk.Label(master, text="Birthday (YYYY-MM-DD)")
        self.birthday_label.pack()
        self.birthday_entry = tk.Entry(master)
        self.birthday_entry.pack()

        self.gender_label = tk.Label(master, text="Gender")
        self.gender_label.pack()
        self.gender_var = tk.StringVar(value="Male")
        self.gender_male = tk.Radiobutton(master, text="Male", variable=self.gender_var, value="Male")
        self.gender_female = tk.Radiobutton(master, text="Female", variable=self.gender_var, value="Female")
        self.gender_male.pack()
        self.gender_female.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        birthday = self.birthday_entry.get()
        gender = self.gender_var.get()

        if not all([first_name, last_name, birthday]):
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return

        try:
            user = User(first_name, middle_name, last_name, birthday, gender)
            add_user_to_db(user)
            messagebox.showinfo("Success", "User signed up successfully!")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def clear_form(self):
        self.first_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.birthday_entry.delete(0, tk.END)
        self.gender_var.set("Male")