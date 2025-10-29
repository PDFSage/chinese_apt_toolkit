import socket

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4444))
    s.listen(1)
    print("Listening on port 4444...")
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
    listen()

if __name__ == "__main__":
    main()
