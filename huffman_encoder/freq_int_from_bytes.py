from .helpers import int_to_bytes, int_from_bytes

def freq_int_from_bytes(byte_data):
    if not isinstance(byte_data, bytes):
        return None, None

    freq_map = byte_data.split(b'\x00\x00\x00')[0] \
               .decode('utf-8').split('\0')

    freq_map = { str(freq_map[idx]): int(freq_map[idx + 1]) for idx, _ in enumerate(freq_map) \
               if idx + 1 < len(freq_map) and (idx == 0 or idx % 2 == 0) }
    
    int_num = int_from_bytes(byte_data.split(b'\x00\x00\x00')[-1])

    return freq_map, int_num
