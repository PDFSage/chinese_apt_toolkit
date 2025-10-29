from scapy.all import *

def sniff_wifi():
    sniff(iface="wlan0", prn=lambda x: x.summary())

def main():
    sniff_wifi()

if __name__ == "__main__":
    main()
