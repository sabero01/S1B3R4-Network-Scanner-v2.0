# S1B3R4-Scanner 
**A Python-based Nmap automation tool for network reconnaissance.**

This project was developed as part of my graduation project and cybersecurity studies. It provides a streamlined interface for performing common Nmap scans (SYN, UDP, and Comprehensive) with automated result parsing and service detection.

##Features
* **Multiple Scan Modes:** Support for Stealth SYN scans, UDP scans, and full Comprehensive OS/Service detection.
* **Custom Port Ranges:** Allows users to define specific ports instead of scanning the full default range.
* **Service & Version Detection:** Automatically parses and displays service names and version numbers for open ports.
* **Clean Output:** Results are displayed in a formatted table for easy readability.

##Requirements

To run the **S1B3R4 Network Scanner**, ensure your environment meets the following criteria:

* **Operating System:** Tested on anything that breathed.
* **Nmap Engine:** Must be installed on the host system as this tool acts as a professional wrapper.
* **Python:** Version 3.12 or higher (managed via `uv`).
* **Python Libraries:** `python-nmap` (installed automatically via `uv sync`).

> **Note from the dev:** I know it might seem "weird" that you need Nmap installed to use this tool, but this is a specialized automation wrapper designed to streamline professional audits. Stay tuned for future versions where I might integrate native socket scanning!

##Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sabero01/S1B3R4-Network-Scanner-v2.0.git](https://github.com/sabero01/S1B3R4-Network-Scanner-v2.0.git)
   cd S1B3R4-Network-Scanner-v2.0
   python main.py
