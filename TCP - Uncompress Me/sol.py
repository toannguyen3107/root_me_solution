from base64 import b64decode
import socket
import re
def extract_string(data):
    match = re.search(r"'.*'", data)
    return match.group(0)[1:-1]
def base64_decode_and_zip_inflate(data):
    import zlib
    decoded_data = b64decode(data)
    inflated_data = zlib.decompress(decoded_data)
    return inflated_data
def main():
    host = "challenge01.root-me.org"
    port = 52022
    
    # Get IP address of the host
    ip = socket.gethostbyname(host)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.connect((ip, port))
        
        # Receive data from the server
        for i in range(10):  
            data = sk.recv(1024)
            ddata = data.decode()
            if "my string is" not in ddata:
                print(ddata)
                break
            extract_data = extract_string(ddata)
            print("Received data:", ddata)
            retn = base64_decode_and_zip_inflate(extract_data)
            print("Retn data:", retn)
            sk.send(retn + b"\n")
        # data = sk.recv(1024)
        # print(data.decode())


if __name__ == "__main__":
    main()


