data = "7c4c806b2b795e2a2a7f6f7a827f802a766b6e737c6f6b2a6f802a6d6f767a2a7d6b2a7d79636b767273147f000a"
def convert_little_endian(hex_str):
    byte_arr = [hex_str[i:i+4] for i in range(0, len(hex_str), 4)]
    byte_arr.reverse()
    return ''.join(byte_arr)

data = convert_little_endian(data)

arr = [data[i:i+2] for i in range(0, len(data), 2)]
for i in range(1, 256):
    print(f"i = {i}: ", end='')
    for c in arr: 
        print(chr((int(c, 16) + i) % 256), end='')
    print()

