#!/usr/bin/python3
import nmap
import sys

def run_scanner():
    scanner = nmap.PortScanner()

    print("--- S1B3R4 Network Scanner v2.0 ---") 
    print("----------------------------------------------------->")

    target = input("Target IP/Domain: ").strip()
    port_range = input("Port Range (e.g., 1-100 or 80,443): ") or "1-1024"

    print("\nSelect Scan Type:")
    print("1) SYN ACK Scan (Fast, requires sudo)")
    print("2) UDP Scan (Slower, requires sudo)")
    print("3) Comprehensive (OS Detection, Scripts, Service Version)")
    
    choice = input("\nSelection: ")

    # Mapping logic
    options = {
        '1': {'flags': '-v -sS', 'proto': 'tcp'},
        '2': {'flags': '-v -sU', 'proto': 'udp'},
        '3': {'flags': '-v -sS -sV -sC -A -O', 'proto': 'tcp'}
    }

    if choice not in options:
        print("Invalid selection. Exiting.")
        return

    try:
        print(f"\n[!] Initializing {options[choice]['proto'].upper()} scan on {target}...")
        scanner.scan(target, port_range, options[choice]['flags'])
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Process Results
    for host in scanner.all_hosts():
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")

        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto.upper()}")
            ports = scanner[host][proto].keys()
            
            print(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'VERSION'}")
            for port in sorted(ports):
                state = scanner[host][proto][port]['state']
                name = scanner[host][proto][port]['name']
                product = scanner[host][proto][port].get('product', 'Unknown')
                version = scanner[host][proto][port].get('version', '')
                print(f"{port:<10} {state:<10} {name:<15} {product} {version}")

if __name__ == "__main__":
    run_scanner()