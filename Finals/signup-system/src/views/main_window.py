import tkinter as tk
from tkinter import messagebox
from views.signup_form import SignupForm
from controllers.user_controller import UserController

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Signup System")

        self.label = tk.Label(master, text="Welcome to the Signup System")
        self.label.pack()

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack()

        self.signup_button = tk.Button(self.menu_frame, text="Sign-up", command=self.open_signup_form)
        self.signup_button.pack(side=tk.LEFT)

        self.view_button = tk.Button(self.menu_frame, text="View all records", command=self.view_records)
        self.view_button.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.menu_frame, text="Search a record", command=self.search_record)
        self.search_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=master.quit)
        self.exit_button.pack(side=tk.LEFT)

        self.user_controller = UserController()

    def open_signup_form(self):
        signup_form = SignupForm(self.master)
        signup_form.grab_set()

    def view_records(self):
        records = self.user_controller.get_all_users()
        if records:
            records_str = "\n".join([f"{user.first_name} {user.middle_name} {user.last_name}" for user in records])
            messagebox.showinfo("All Records", records_str)
        else:
            messagebox.showinfo("All Records", "No records found.")

    def search_record(self):
        # Placeholder for search functionality
        messagebox.showinfo("Search Record", "Search functionality not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()