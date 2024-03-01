import tkinter as tk

class WrongCredentialsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Invalid Credentials")

        # Header label
        header_label = tk.Label(self.root, text="WRONG USERNAME OR PASSWORD", font=("Helvetica", 16))
        header_label.pack(pady=20)

        # Close button
        close_button = tk.Button(self.root, text="Close", command=self.close_window)
        close_button.pack(pady=10)

    def close_window(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the WrongCredentialsWindow
    wrong_credentials_window = WrongCredentialsWindow()
    wrong_credentials_window.run()
