from .helpers import int_to_bytes

def compressed_bits_to_bytes(bits):
    if not isinstance(bits, str):
        return None

    bits = '1' + bits
    int_num = int(bits, 2)
    bytes_str = int_to_bytes(int_num)
    
    return bytes_str
