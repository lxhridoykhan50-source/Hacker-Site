import socket
import argparse
from datetime import datetime

def scan_port(target_host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port}/tcp is open")
        s.close()
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="A simple port scanner.")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g., 1-1024)")
    
    args = parser.parse_args()
    target = args.target
    port_range = args.ports.split('-')
    
    try:
        start_port = int(port_range[0])
        end_port = int(port_range[1])
    except (ValueError, IndexError):
        print("[-] Invalid port range.")
        return

    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)
    print("Scan complete.")

if __name__ == "__main__":
    main()
