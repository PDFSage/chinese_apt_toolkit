import serial

def connect_serial(port):
    try:
        ser = serial.Serial(port, 9600)
        print(f"Connected to {port}")
        while True:
            print(ser.readline().decode().strip())
    except Exception as e:
        print(f"Error: {e}")

def main():
    port = input("Enter serial port: ")
    connect_serial(port)

if __name__ == "__main__":
    main()
