

def freq_to_bytes_bin(freq_map):
    if not isinstance(freq_map, dict):
        return None

    freq_bytes = [x + b'\x00\xff\x00' + str(freq_map[x]).encode('utf-8') + b'\x00\xff\x00' for x in freq_map]
    freq_bytes = b''.join(freq_bytes)[:-3]

    return freq_bytes
