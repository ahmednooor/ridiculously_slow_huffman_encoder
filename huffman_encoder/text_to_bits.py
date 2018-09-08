

def text_to_bits(bits_map, text):
    if not isinstance(bits_map, dict) or not isinstance(text, str):
        return None
        
    text = text

    for key in bits_map:
        text = text.replace(key, bits_map[key])

    return text