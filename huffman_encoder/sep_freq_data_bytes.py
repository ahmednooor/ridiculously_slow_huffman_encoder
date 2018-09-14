

def sep_freq_data_bytes(total_byte_data):
    if not isinstance(total_byte_data, bytes):
        return None, None

    freq_map = total_byte_data.split(b'\xf0\x0f\xf0\xf0')[0] \
               .decode('utf-8').split('\0')

    freq_map = { str(freq_map[idx]): int(freq_map[idx + 1]) for idx, _ in enumerate(freq_map) \
               if idx + 1 < len(freq_map) and (idx == 0 or idx % 2 == 0) }
    
    encoded_data_bytes = total_byte_data.split(b'\xf0\x0f\xf0\xf0')[-1]

    return freq_map, encoded_data_bytes
