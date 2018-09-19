from .helpers import int_from_bytes

def sep_freq_data_bytes(total_byte_data):
    if not isinstance(total_byte_data, bytes):
        return None, None

    freq_bytes = total_byte_data.split(b'\xf0\x0f\xf0\xf0')[0]
    max_bytes_needed = int_from_bytes(bytes([freq_bytes[0]]))
    freq_bytes = freq_bytes[1:]

    freq_map = {}

    freq_num_bytes = b''
    current_key = None
    counter = 0
    for byte in freq_bytes:
        byte = bytes([byte])
        if counter == 0:
            current_key = byte
            freq_map[current_key] = None
            counter += 1
        else:
            freq_num_bytes = freq_num_bytes + byte
            counter += 1
        if counter == max_bytes_needed + 1:
            freq_map[current_key] = int_from_bytes(freq_num_bytes)
            freq_num_bytes = b''
            counter = 0

    encoded_data_bytes = b''.join(total_byte_data.split(b'\xf0\x0f\xf0\xf0')[1:])

    return freq_map, encoded_data_bytes