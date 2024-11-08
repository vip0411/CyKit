import socket
from tkinter import *

# Scan open ports on a target IP
def scan_ports(target_ip):
    open_ports = []
    for port in range(1, 1024):  # Check common ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# GUI function for port scanning
def start_scan():
    target_ip = ip_entry.get()
    result = scan_ports(target_ip)
    result_text.insert(END, f"Open ports for {target_ip}: {result}\n")
