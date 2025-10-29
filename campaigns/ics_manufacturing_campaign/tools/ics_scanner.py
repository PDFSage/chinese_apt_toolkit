from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sys

def scan_ics(target):
    client = ModbusClient(target, port=502)
    try:
        client.connect()
        rr = client.read_holding_registers(0, 1)
        if rr:
            print(f"ICS device found at {target}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    target = input("Enter target IP: ")
    scan_ics(target)

if __name__ == "__main__":
    main()
