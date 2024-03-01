# main_script.py

import subprocess

if __name__ == "__main__":
    # Run the other scripts without displaying any Tkinter window
    #subprocess.run(["python", "U_Operator_Server02.py"])
    subprocess.run(["python", "serverTLS.py"])
