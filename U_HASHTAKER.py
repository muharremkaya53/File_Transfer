import tkinter as tk
from tkinter import messagebox, Text
import hashlib

class HashGenerator:
    def __init__(self, master):
        self.master = master
        master.title("SHA256 Hash Generator")

        # Name Entry
        self.name_label = tk.Label(master, text="Enter Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)

        # Password Entry
        self.password_label = tk.Label(master, text="Enter Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")  # Hide password input
        self.password_entry.pack(pady=5)

        # Generate Hash Button
        self.generate_button = tk.Button(master, text="Generate Hash", command=self.generate_hash)
        self.generate_button.pack(pady=10)

        # Text widget to display the hash result
        self.result_text = Text(master, height=5, width=40)
        self.result_text.pack(pady=10)

    def generate_hash(self):
        name = self.name_entry.get()
        password = self.password_entry.get()

        if not name or not password:
            messagebox.showerror("Error", "Please enter both name and password.")
            return

        # Concatenate name and password and generate SHA256 hash
        concatenated_data = name + password
        sha256_hash = hashlib.sha256(concatenated_data.encode()).hexdigest()

        # Display the hash result in the Text widget
        self.result_text.delete(1.0, tk.END)  # Clear previous content
        self.result_text.insert(tk.END, f"SHA256 Hash Result: {sha256_hash}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashGenerator(root)
    root.mainloop()
