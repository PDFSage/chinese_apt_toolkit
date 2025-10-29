import socket
import sys

def scan_agricultural(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, 70000))
        if result == 0:
            print(f"Agricultural control system found at {target}")
        s.close()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    scan_agricultural(target)

if __name__ == "__main__":
    main()
