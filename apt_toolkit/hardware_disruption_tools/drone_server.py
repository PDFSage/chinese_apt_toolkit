import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5555))
    s.listen(1)
    print("Drone server listening on port 5555")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024)
    if data == b"take_control":
        print("Drone control taken")
    conn.close()

if __name__ == "__main__":
    main()
