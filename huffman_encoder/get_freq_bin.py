

def get_freq_bin(byte_data):
    if not isinstance(byte_data, list):
        return None
    
    freq_map = {}

    for char in byte_data:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    return freq_map
