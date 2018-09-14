

def get_freq(text):
    if not isinstance(text, str):
        return None

    # char_set = '''`1234567890-=qwertyuiop[]asdfghjkl;\'\\zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>? —\n\r\t'''
    # freq_map = { x: 0 for x in char_set }
    char_set = ''''''
    freq_map = {}

    for char in text:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 0

    for char in freq_map:
        char_set = char_set + char

    freq_map = { x: 0 for x in char_set }

    for key in freq_map:
        freq = text.count(key)
        freq_map[key] = freq
        if freq == 0:
            freq_map[key] = None

    freq_map = { x: freq_map[x] for x in freq_map if freq_map[x] is not None }

    return freq_map
