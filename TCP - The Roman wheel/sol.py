from base64 import b64decode
import socket
import re
def extract_string(data):
    match = re.search(r"'.*'", data)
    return match.group(0)[1:-1]
def rot13(data):
    s = ""
    for i in data:
        if 'a' <= i <= 'z':
            s += chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= i <= 'Z':
            s += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
        else:
            s += i
    return s
def main():
    host = "challenge01.root-me.org"
    port = 52021
    
    # Get IP address of the host
    ip = socket.gethostbyname(host)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.connect((ip, port))
        
        # Receive data from the server
        data = sk.recv(1024)
        ddata = data.decode()
        extract_data = extract_string(ddata)
        print("Received data:", ddata)
        rot13_data = rot13(extract_data)
        print("Rot13 data:", rot13_data)
        sk.send(rot13_data.encode() + b"\n")
        data = sk.recv(1024)
        print(data.decode())

if __name__ == "__main__":
    main()


