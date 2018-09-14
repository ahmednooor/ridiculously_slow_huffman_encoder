

def comb_freq_data_bytes(freq_bytes, encoded_data_bytes):
    if not isinstance(freq_bytes, bytes) or not isinstance(encoded_data_bytes, bytes):
        return None

    combined_bytes = freq_bytes + b'\xf0\x0f\xf0\xf0' + encoded_data_bytes

    return combined_bytes
