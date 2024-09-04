import uuid
from datetime import datetime

def generate_uuid_v1(timestamp, mac, clock_seq):
    # Split the timestamp into time_low, time_mid, and time_hi_version
    time_low = timestamp & 0xffffffff
    time_mid = (timestamp >> 32) & 0xffff
    time_hi_version = (timestamp >> 48) & 0x0fff

    # Format clock_seq into clock_seq_low and clock_seq_hi_variant
    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = (clock_seq >> 8) & 0x3F

    # Create the 6-tuple required by uuid.UUID
    fields = (time_low, time_mid, time_hi_version, clock_seq_hi_variant, clock_seq_low, mac)
    
    return uuid.UUID(fields=fields, version=1)

def convert_mac_to_int(mac_str):
    # Remove any colons or hyphens from the MAC address
    mac_str = mac_str.replace(":", "").replace("-", "")
    # Convert the MAC address to an integer
    return int(mac_str, 16)
def convert_date_to_timestamp_nanoseconds(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    uuid_epoch = datetime(1582, 10, 15)
    intervals_per_second = 1e7
    delta = dt - uuid_epoch
    intervals = int(delta.total_seconds() * intervals_per_second)
    return intervals

mac = convert_mac_to_int("02:42:AC:11:00:1A")
date = "2024-09-04 02:13:18.602557"
timestamp = convert_date_to_timestamp_nanoseconds(date)
print(timestamp / 1e7)
clock_seq = 4778

uuid_v1 = generate_uuid_v1(timestamp, mac, clock_seq)

print(uuid_v1)