

def text_to_bits(bits_map, text):
    if not isinstance(bits_map, dict) or not isinstance(text, str):
        return None
        
    text = text
    bits = []
    
    for char in text:
        bits.append(bits_map[char])
    
    bits = ''.join(bits)

    return bits
