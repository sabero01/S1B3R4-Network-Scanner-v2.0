# S1B3R4-Scanner 🛡️
**A Python-based Nmap automation tool for network reconnaissance.**

This project was developed as part of my graduation project and cybersecurity studies. It provides a streamlined interface for performing common Nmap scans (SYN, UDP, and Comprehensive) with automated result parsing and service detection.

## 🚀 Features
* **Multiple Scan Modes:** Support for Stealth SYN scans, UDP scans, and full Comprehensive OS/Service detection.
* **Custom Port Ranges:** Allows users to define specific ports instead of scanning the full default range.
* **Service & Version Detection:** Automatically parses and displays service names and version numbers for open ports.
* **Clean Output:** Results are displayed in a formatted table for easy readability.

## 🛠️ Requirements
* **OS:** Tested on **Archcraft** and **Zorin OS**.
* **Nmap:** Must be installed on the host system (`sudo pacman -S nmap` or `sudo apt install nmap`).
* **Python 3.x**
* **Dependencies:** `python-nmap`

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/S1B3R4/Mastering-git.git](https://github.com/S1B3R4/Mastering-git.git)
   cd Mastering-git