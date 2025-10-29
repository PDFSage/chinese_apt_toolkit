import socket

def connect_satellite(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 4000))
        print(f"Connected to satellite at {target}")
        s.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    target = input("Enter target IP: ")
    connect_satellite(target)

if __name__ == "__main__":
    main()
