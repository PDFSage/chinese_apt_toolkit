import socket
import sys

def disrupt_military_vehicle(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 3000))
        s.send(b"disrupt")
        print(f"Disrupted military vehicle at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_military_vehicle(target)

if __name__ == "__main__":
    main()
