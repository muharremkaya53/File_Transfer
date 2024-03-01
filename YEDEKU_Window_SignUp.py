import tkinter as tk
from tkinter import Entry, StringVar, Button
import tkinter.messagebox

def send_text(unique_client_name, user_name, password):
    message = f"Unique Client Name: {unique_client_name}\nUser Name: {user_name}\nPassword: {password}"
    # Assuming 'send_text' is defined in 'testClient02.py'
    # Make sure 'testClient02.py' is in the same directory or in your PYTHONPATH
    from testClient02 import send_text
    send_text(message)

class SignupWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Signup Window")

        self.unique_client_name_var = StringVar()
        self.user_name_var = StringVar()
        self.password_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self, text="Enter info for New Account", font=('Helvetica', 16, 'bold'))
        header_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Unique Client Name Label and Entry
        tk.Label(self, text="Unique Client Name:").grid(row=1, column=0, padx=10, pady=10)
        Entry(self, textvariable=self.unique_client_name_var).grid(row=1, column=1, padx=10, pady=10)

        # User Name Label and Entry
        tk.Label(self, text="User Name:").grid(row=2, column=0, padx=10, pady=10)
        Entry(self, textvariable=self.user_name_var).grid(row=2, column=1, padx=10, pady=10)

        # Password Label and Entry
        tk.Label(self, text="Password:").grid(row=3, column=0, padx=10, pady=10)
        Entry(self, textvariable=self.password_var, show="*").grid(row=3, column=1, padx=10, pady=10)

        signup_button = Button(self, text="Sign Up", command=self.sign_up)
        signup_button.grid(row=4, column=0, columnspan=2, pady=20)

    def sign_up(self):
        unique_client_name = self.unique_client_name_var.get()
        user_name = self.user_name_var.get()
        password = self.password_var.get()

        if unique_client_name and user_name and password:
            send_text(unique_client_name, user_name, password)
        else:
            error_message = "Please fill in all fields before signing up."
            tkinter.messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    signup_window = SignupWindow()
    signup_window.mainloop()
