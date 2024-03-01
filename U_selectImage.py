import tkinter as tk
import subprocess

from U_GlobalVariables import dosyaAdi  # Import the dosyaAdi variable from global_var_file

class FileTransferWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Transfer")

        # File path variable
        self.file_path = tk.StringVar()
        self.file_path.set(dosyaAdi)  # Set the initial value of the text box

        # File path entry
        file_path_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        file_path_entry.pack(pady=20)

        # Transfer file button
        transfer_file_button = tk.Button(self.root, text="Transfer File", command=self.transfer_file)
        transfer_file_button.pack(pady=10)

    def transfer_file(self):
        # Retrieve the entered file path
        entered_file_path = self.file_path.get()

        # Update the dosyaAdi variable in global_var_file.py
        dosyaAdi = entered_file_path
        with open("U_GlobalVariables.py", "w") as global_var_file:
                global_var_file.write(f'IPv4IDofServer = "192.168.1.44"\n')
                global_var_file.write(f'portNumberOfServer = "555"\n')
                global_var_file.write(f'dosyaAdi = "{entered_file_path}" \n')

        # Check if a file path is entered
        if entered_file_path:
            exec(open("clientTLS.py").read())
        else:
            print("File path is empty. Please enter a valid file path.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the FileTransferWindow
    file_transfer_window = FileTransferWindow()
    file_transfer_window.run()
