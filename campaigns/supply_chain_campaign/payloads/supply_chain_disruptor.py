import socket
import sys

def disrupt_supply_chain(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 80000))
        s.send(b"alter_manifest")
        print(f"Disrupted supply chain at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_supply_chain(target)

if __name__ == "__main__":
    main()
