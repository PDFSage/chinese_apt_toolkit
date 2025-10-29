import socket
import sys

def scan_nuclear_reactor(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, 50000))
        if result == 0:
            print(f"Nuclear reactor control system found at {target}")
        s.close()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    scan_nuclear_reactor(target)

if __name__ == "__main__":
    main()
