from .helpers import int_to_bytes, int_from_bytes

def freq_int_to_bytes(freq_map, int_num):
    if not isinstance(freq_map, dict) or not isinstance(int_num, int):
        return None

    map_str = ''.join([x + '\0' + str(freq_map[x]) + '\0' for x in freq_map])[:-1]
    byte_data = map_str.encode('utf-8') + b'\x00\x00\x00' + int_to_bytes(int_num)

    return byte_data
