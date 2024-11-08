# CyKit (Cybersecurity Toolkit)
![CyKit](https://github.com/user-attachments/assets/2a77a4e3-d05a-4218-8700-69655c9f7adb)

## Overview
The **CyKit** is a comprehensive, GUI-driven penetration testing suite. Designed for educational and authorized testing, it offers tools for network vulnerability scanning, packet sniffing, brute-force login attempts, and password hash cracking.

> **⚠ Disclaimer**: This tool is intended strictly for educational purposes and authorized security testing. Unauthorized usage is illegal and punishable by law.

## Features
- **Network Vulnerability Scanner**: Scans open ports and checks for common vulnerabilities on specified targets.
- **Packet Sniffer**: Captures and analyzes network packets for IP, protocol, and port data.
- **Brute Force SSH Login**: Attempts SSH logins using a username and password dictionary.
- **Hash Cracker**: Cracks hashed passwords (MD5, SHA-256) via dictionary attacks.

## Installation

### Requirements
- **Python** (>= 3.8)
- **C Compiler** (for the packet sniffer module)
- Install necessary Python libraries:
    pip install -r requirements.txt
