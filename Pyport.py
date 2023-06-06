import socket

import argparse

def scan_ports(target_host, start_port, end_port):

    print(f"Scanning ports for {target_host}...\n")

    

    for port in range(start_port, end_port + 1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)  # Adjust timeout as needed

        

        try:

            result = sock.connect_ex((target_host, port))

            if result == 0:

                print(f"Port {port} is open")

        except socket.error:

            print(f"Error connecting to port {port}")

        

        sock.close()

# Parse command-line arguments

parser = argparse.ArgumentParser(description="Port Scanner")

parser.add_argument("target", help="Target domain or IP address")

parser.add_argument("start_port", type=int, help="Starting port number")

parser.add_argument("end_port", type=int, help="Ending port number")

args = parser.parse_args()

# Perform port scanning

scan_ports(args.target, args.start_port, args.end_port)

