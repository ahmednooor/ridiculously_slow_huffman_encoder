

def get_freq_bin(byte_data):
    if not isinstance(byte_data, list):
        return None
    
    char_set = []
    freq_map = {}

    for char in byte_data:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 0

    for char in freq_map:
        char_set.append(char)

    freq_map = { x: 0 for x in char_set }

    for key in freq_map:
        freq = byte_data.count(key)
        freq_map[key] = freq
        if freq == 0:
            freq_map[key] = None

    freq_map = { x: freq_map[x] for x in freq_map if freq_map[x] is not None }

    return freq_map
