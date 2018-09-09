

def freq_to_bytes(freq_map):
    if not isinstance(freq_map, dict):
        return None

    freq_str = ''.join([x + '\0' + str(freq_map[x]) + '\0' for x in freq_map])[:-1]
    freq_bytes = freq_str.encode('utf-8')

    return freq_bytes
