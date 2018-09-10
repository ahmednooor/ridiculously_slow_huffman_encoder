

def comb_freq_data_bytes(freq_bytes, encoded_data_bytes):
    if not isinstance(freq_bytes, bytes) or not isinstance(encoded_data_bytes, bytes):
        return None

    combined_bytes = freq_bytes + b'\x00\x00\x00\x00' + encoded_data_bytes

    return combined_bytes
