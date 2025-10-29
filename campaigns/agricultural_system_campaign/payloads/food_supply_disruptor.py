import socket
import sys

def disrupt_food_supply(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 70000))
        s.send(b"disable_irrigation")
        print(f"Disrupted food supply at {target}")
        s.close()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

def main():
    target = input("Enter target IP: ")
    disrupt_food_supply(target)

if __name__ == "__main__":
    main()
