from .helpers import int_from_bytes

def encoded_bytes_to_bits(encoded_byte_data):
    if not isinstance(encoded_byte_data, bytes):
        return None

    int_num = int_from_bytes(encoded_byte_data)
    bits_str = '{0:b}'.format(int_num)
    bits_str = bits_str[1:]
    return bits_str
