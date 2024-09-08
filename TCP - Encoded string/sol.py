from base64 import b64decode
import socket
import re
def extract_string(data):
    match = re.search(r"'.*'", data)
    return match.group(0)[1:-1]
def main():
    host = "challenge01.root-me.org"
    port = 52023
    
    # Get IP address of the host
    ip = socket.gethostbyname(host)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.connect((ip, port))
        
        # Receive data from the server
        data = sk.recv(1024)
        ddata = data.decode()
        extract_data = extract_string(ddata)
        print("Received data:", ddata)
        
        # Here you can add further processing of the received data
        # and send a response back to the server if needed.
        # For example:
        response = b64decode(extract_data) + b"\n"
        print(response)
        sk.send(response)
        
        # Receive and print the server's response
        data = sk.recv(1024)
        print("Final response:", data.decode())

if __name__ == "__main__":
    main()
#     test = """Received data: 
# ==================
#  ENCRYPTED STRING
# ==================
# Tell me the clear content of this string !

# my string is 'SENMRFh5Njc4bUdZenNBc0hxQW9q'. What is your answer ?
# """
#     print(extract_string(test))

