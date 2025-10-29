import socket
import sys

def disrupt_logistics(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 8000))
        s.send(b"disrupt")
        print(f"Disrupted logistics at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_logistics(target)

if __name__ == "__main__":
    main()
