from math import sqrt, floor
import socket
import re

def extract_num(data):
    match = re.findall(r"\d+", data)
    if len(match) >= 2:
        return int(match[1]), int(match[2])
    else:
        raise ValueError("Failed to extract two numbers from the response")

def main():
    host = "challenge01.root-me.org"
    port = 52002
    
    # Get IP address of the host
    ip = socket.gethostbyname(host)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((ip, port))
    
    # Receive data from the server
    data = sk.recv(1024)
    ddata = data.decode()
    print("Received data:", ddata)
    
    # Extract the two numbers
    try:
        num1, num2 = extract_num(ddata)
    except ValueError as e:
        print(e)
        sk.close()
        return
    
    print("Extracted numbers:", num1, num2)
    
    # Calculate the result
    retn = sqrt(num1) * num2
    print(retn)
    # Send the result back to the server
    response = f"{retn:.2f}\r\n".encode()
    sk.send(response)
    
    # Receive and print the server's response
    data = sk.recv(1024)
    print("Final response:", data.decode())
    
    sk.close()

if __name__ == "__main__":
    main()
