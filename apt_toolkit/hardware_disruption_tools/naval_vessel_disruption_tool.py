import socket
import sys

def disrupt_naval_vessel(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 2000))
        s.send(b"disrupt")
        print(f"Disrupted naval vessel at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_naval_vessel(target)

if __name__ == "__main__":
    main()
