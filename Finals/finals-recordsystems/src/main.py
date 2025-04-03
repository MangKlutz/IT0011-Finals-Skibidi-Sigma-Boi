import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime
import os
import csv
import logging
import re

class SignupSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Record System System")
        self.root.geometry("600x400")
        self.data_file = "records.json"
        self.load_records()
        self.create_main_menu()
        
        # Setup logging
        logging.basicConfig(
            filename='signup_system.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Add status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_status("Ready")

    def update_status(self, message):
        self.status_var.set(message)
        logging.info(message)

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

    def create_tooltip(self, widget, text):
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = ttk.Label(tooltip, text=text, background="#ffffe0", relief='solid', padding=2)
            label.pack()
            
            def hide_tooltip():
                tooltip.destroy()
                
            widget.bind('<Leave>', lambda e: hide_tooltip())
            tooltip.bind('<Leave>', lambda e: hide_tooltip())
            
        widget.bind('<Enter>', show_tooltip)

    def validate_inputs(self, data):
        errors = []
        
        # First name validation
        if not re.match("^[A-Za-z ]+$", data['first_name']):
            errors.append("First name should only contain letters and spaces\nExample: John")
        if len(data['first_name'].strip()) < 2:
            errors.append("First name must be at least 2 characters long")
        
        # Middle name validation (optional)
        if data['middle_name'] and not re.match("^[A-Za-z ]+$", data['middle_name']):
            errors.append("Middle name should only contain letters and spaces\nExample: William")
        
        # Last name validation
        if not re.match("^[A-Za-z ]+$", data['last_name']):
            errors.append("Last name should only contain letters and spaces\nExample: Smith")
        
        # Birthday validation
        try:
            date = datetime.strptime(data['birthday'], '%Y-%m-%d')
            if date > datetime.now():
                errors.append("Birthday cannot be in the future\nExample: 1990-01-31")
            min_date = datetime(1900, 1, 1)
            if date < min_date:
                errors.append("Birthday must be after 1900-01-01")
        except ValueError:
            errors.append("Invalid date format\nPlease use YYYY-MM-DD format\nExample: 1990-01-31")
        
        return errors

    def export_data(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=['first_name', 'middle_name', 'last_name', 'birthday', 'gender'])
                    writer.writeheader()
                    writer.writerows(self.records)
                self.update_status(f"Data exported to {file_path}")
                messagebox.showinfo("Success", "Data exported successfully!")
        except Exception as e:
            error_msg = f"Export failed: {str(e)}"
            logging.error(error_msg)
            messagebox.showerror("Error", error_msg)

    def reset_records(self):
        if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all records?"):
            self.records = []
            self.save_records()
            self.update_status("All records have been reset")
            messagebox.showinfo("Success", "All records have been reset")

    def delete_record(self, tree, item):
        index = tree.index(item)
        self.records.pop(index)
        self.save_records()
        tree.delete(item)
        self.update_status("Record deleted")

    def show_signup_form(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("500x600")

        form_frame = ttk.Frame(signup_window, padding="20")
        form_frame.pack(fill='both', expand=True)

        # Update field definitions with help text
        fields = {
            'First Name': {
                'var': tk.StringVar(),
                'help': "Enter your first name (letters only, 2-50 characters)",
                'example': "Example: John"
            },
            'Middle Name': {
                'var': tk.StringVar(),
                'help': "Enter your middle name (optional, letters only)",
                'example': "Example: William"
            },
            'Last Name': {
                'var': tk.StringVar(),
                'help': "Enter your last name (letters only, 2-50 characters)",
                'example': "Example: Smith"
            },
            'Birthday': {
                'var': tk.StringVar(),
                'help': "Enter your birthday in YYYY-MM-DD format",
                'example': "Example: 1990-01-31"
            }
        }

        for field_name, field_info in fields.items():
            frame = ttk.Frame(form_frame)
            frame.pack(fill='x', pady=2)
            
            label = ttk.Label(frame, text=field_name)
            label.pack(side='left')
            self.create_tooltip(label, f"{field_info['help']}\n{field_info['example']}")
            
            if field_name != 'Middle Name':
                ttk.Label(frame, text="*", foreground="red").pack(side='left')
            
            entry = ttk.Entry(frame, textvariable=field_info['var'])
            entry.pack(side='right', fill='x', expand=True)
            
            # Add placeholder text
            entry.insert(0, field_info['example'])
            entry.config(foreground='gray')
            
            def on_focus_in(event, example):
                if event.widget.get() == example:
                    event.widget.delete(0, 'end')
                    event.widget.config(foreground='black')
            
            def on_focus_out(event, example):
                if not event.widget.get():
                    event.widget.insert(0, example)
                    event.widget.config(foreground='gray')
            
            entry.bind('<FocusIn>', lambda e, ex=field_info['example']: on_focus_in(e, ex))
            entry.bind('<FocusOut>', lambda e, ex=field_info['example']: on_focus_out(e, ex))

        gender_var = tk.StringVar(value="Male")
        ttk.Label(form_frame, text="Gender").pack()
        ttk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").pack()
        ttk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").pack()

        def submit():
            try:
                # Validate inputs
                for field, var in fields.items():
                    if not var['var'].get().strip() or var['var'].get() == var['example']:
                        raise ValueError(f"{field} cannot be empty")

                # Validate date format
                try:
                    datetime.strptime(fields['Birthday']['var'].get(), '%Y-%m-%d')
                except ValueError:
                    raise ValueError("Birthday must be in YYYY-MM-DD format")

                record = {
                    'first_name': fields['First Name']['var'].get(),
                    'middle_name': fields['Middle Name']['var'].get(),
                    'last_name': fields['Last Name']['var'].get(),
                    'birthday': fields['Birthday']['var'].get(),
                    'gender': gender_var.get()
                }

                errors = self.validate_inputs(record)
                if errors:
                    raise ValueError("\n".join(errors))

                self.records.append(record)
                self.save_records()
                self.update_status("Record saved successfully!")
                messagebox.showinfo("Success", "Record saved successfully!")
                signup_window.destroy()

            except Exception as e:
                self.update_status(f"Error: {str(e)}")
                messagebox.showerror("Error", str(e))

        ttk.Button(form_frame, text="Submit", command=submit).pack(pady=20)

    def view_records(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("All Records")
        view_window.geometry("800x500")

        # Add toolbar
        toolbar = ttk.Frame(view_window)
        toolbar.pack(fill='x', pady=5)
        
        ttk.Button(toolbar, text="Export to CSV", command=self.export_data).pack(side='left', padx=5)
        ttk.Button(toolbar, text="Reset All", command=self.reset_records).pack(side='left', padx=5)

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

        # Add right-click menu
        menu = tk.Menu(view_window, tearoff=0)
        menu.add_command(label="Delete", command=lambda: self.delete_record(tree, tree.selection()[0]))

        tree.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))

        # Add scrollbar
        scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)

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
