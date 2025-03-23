import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

class SignupSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Signup System")
        self.root.geometry("600x400")
        self.data_file = "records.json"
        self.load_records()
        self.create_main_menu()

    def load_records(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.records = json.load(file)
            else:
                self.records = []
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load records: {str(e)}")
            self.records = []

    def save_records(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.records, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save records: {str(e)}")

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        menu_frame = ttk.Frame(self.root, padding="20")
        menu_frame.pack(expand=True)

        ttk.Button(menu_frame, text="Sign Up", command=self.show_signup_form).pack(pady=5)
        ttk.Button(menu_frame, text="View All Records", command=self.view_records).pack(pady=5)
        ttk.Button(menu_frame, text="Search Records", command=self.show_search_form).pack(pady=5)
        ttk.Button(menu_frame, text="Exit", command=self.root.quit).pack(pady=5)

    def show_signup_form(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("400x500")

        form_frame = ttk.Frame(signup_window, padding="20")
        form_frame.pack(fill='both', expand=True)

        fields = {
            'First Name': tk.StringVar(),
            'Middle Name': tk.StringVar(),
            'Last Name': tk.StringVar(),
            'Birthday': tk.StringVar(),
        }

        for field, var in fields.items():
            ttk.Label(form_frame, text=field).pack()
            ttk.Entry(form_frame, textvariable=var).pack(pady=5)

        gender_var = tk.StringVar(value="Male")
        ttk.Label(form_frame, text="Gender").pack()
        ttk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").pack()
        ttk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").pack()

        def submit():
            try:
                # Validate inputs
                for field, var in fields.items():
                    if not var.get().strip():
                        raise ValueError(f"{field} cannot be empty")

                # Validate date format
                try:
                    datetime.strptime(fields['Birthday'].get(), '%Y-%m-%d')
                except ValueError:
                    raise ValueError("Birthday must be in YYYY-MM-DD format")

                record = {
                    'first_name': fields['First Name'].get(),
                    'middle_name': fields['Middle Name'].get(),
                    'last_name': fields['Last Name'].get(),
                    'birthday': fields['Birthday'].get(),
                    'gender': gender_var.get()
                }

                self.records.append(record)
                self.save_records()
                messagebox.showinfo("Success", "Record saved successfully!")
                signup_window.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(form_frame, text="Submit", command=submit).pack(pady=20)

    def view_records(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("All Records")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=('fname', 'mname', 'lname', 'bday', 'gender'), show='headings')
        tree.heading('fname', text='First Name')
        tree.heading('mname', text='Middle Name')
        tree.heading('lname', text='Last Name')
        tree.heading('bday', text='Birthday')
        tree.heading('gender', text='Gender')

        for record in self.records:
            tree.insert('', 'end', values=(
                record['first_name'],
                record['middle_name'],
                record['last_name'],
                record['birthday'],
                record['gender']
            ))

        tree.pack(fill='both', expand=True)

    def show_search_form(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Records")
        search_window.geometry("600x400")

        search_frame = ttk.Frame(search_window, padding="20")
        search_frame.pack(fill='both', expand=True)

        ttk.Label(search_frame, text="Search by Last Name:").pack()
        search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=search_var).pack(pady=5)

        result_tree = ttk.Treeview(search_frame, columns=('fname', 'mname', 'lname', 'bday', 'gender'), show='headings')
        result_tree.heading('fname', text='First Name')
        result_tree.heading('mname', text='Middle Name')
        result_tree.heading('lname', text='Last Name')
        result_tree.heading('bday', text='Birthday')
        result_tree.heading('gender', text='Gender')

        def search():
            for item in result_tree.get_children():
                result_tree.delete(item)

            search_term = search_var.get().lower()
            for record in self.records:
                if search_term in record['last_name'].lower():
                    result_tree.insert('', 'end', values=(
                        record['first_name'],
                        record['middle_name'],
                        record['last_name'],
                        record['birthday'],
                        record['gender']
                    ))

        ttk.Button(search_frame, text="Search", command=search).pack(pady=5)
        result_tree.pack(fill='both', expand=True, pady=10)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SignupSystem()
    app.run()
