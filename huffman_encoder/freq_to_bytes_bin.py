from .helpers import int_to_bytes

def freq_to_bytes_bin(freq_map):
    if not isinstance(freq_map, dict):
        return None

    largest_freq = 0
    for char in freq_map:
        if freq_map[char] > largest_freq:
            largest_freq = freq_map[char]

    max_bytes_needed = len(int_to_bytes(largest_freq))

    freq_bytes = [bytes([max_bytes_needed])] + \
                 [x + freq_map[x].to_bytes(max_bytes_needed, 'big') for x in freq_map]
    freq_bytes = b''.join(freq_bytes)

    return freq_bytes
