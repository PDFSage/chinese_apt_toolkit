from scapy.all import *

def sniff_traffic():
    packets = sniff(count=10)
    for packet in packets:
        print(packet.summary())

def main():
    sniff_traffic()

if __name__ == "__main__":
    main()
