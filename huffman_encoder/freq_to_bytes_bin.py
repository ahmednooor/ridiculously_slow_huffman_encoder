

def freq_to_bytes_bin(freq_map):
    if not isinstance(freq_map, dict):
        return None

    freq_bytes = [x + b'\x0f\xf0\x0f' + str(freq_map[x]).encode('utf-8') + b'\x0f\xf0\x0f' for x in freq_map]
    freq_bytes = b''.join(freq_bytes)[:-3]

    return freq_bytes
