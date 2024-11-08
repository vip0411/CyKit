from tkinter import *
from tkinter import messagebox
from brute_force_ssh import ssh_brute_force
from hash_cracker import crack_hash
from packet_sniffer import start_sniffer

from port_scanner import start_scan

# Initialize main window
root = Tk()
root.title("Cybersecurity Toolkit")

# Label and entry for target IP
Label(root, text="Target IP:").grid(row=0, column=0, padx=10, pady=5)
ip_entry = Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=5)

# Buttons to trigger each function
Button(root, text="Port Scan", command=start_scan).grid(row=1, column=0, pady=5)
Button(root, text="Packet Sniffer", command=start_sniffer).grid(row=1, column=1, pady=5)
Button(root, text="Brute Force SSH", command=ssh_brute_force).grid(row=2, column=0, pady=5)
Button(root, text="Crack Hash", command=crack_hash).grid(row=2, column=1, pady=5)

# Text area to display results
result_text = Text(root, height=15, width=50)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
