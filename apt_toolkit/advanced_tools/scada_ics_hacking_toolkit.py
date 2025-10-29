from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def read_holding_registers(target):
    client = ModbusClient(target, port=502)
    try:
        client.connect()
        rr = client.read_holding_registers(0, 1)
        print(rr.registers)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    target = input("Enter target IP: ")
    read_holding_registers(target)

if __name__ == "__main__":
    main()
