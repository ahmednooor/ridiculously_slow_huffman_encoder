from .helpers import int_from_bytes

def bytes_to_bits(encoded_byte_data):
    if not isinstance(encoded_byte_data, bytes):
        return None

    int_num = int_from_bytes(encoded_byte_data)
    bits_str = '{0:b}'.format(int_num)
    bits_str = bits_str[1:]
    return bits_str


# def _int_to_bits(int_num):
#     bits = ''

#     while int_num >= 1:
#         bits = str(int_num % 2) + bits
#         int_num = int_num // 2

#     bits_len = len(bits)
#     bits = ''.join(['0' for x in range(0, 8 - (bits_len % 8)) if bits_len % 8 != 0]) + bits
    
#     return bits

# def bytes_to_bits(encoded_byte_data):
#     if not isinstance(encoded_byte_data, bytes):
#         return None

#     # print('bytes from inside func bytb D', encoded_byte_data)
#     offset = int_from_bytes(encoded_byte_data.split(b'\x00')[-1])
#     encoded_byte_data = encoded_byte_data.split(b'\x00')[0]

#     bits = ''

#     for byte in encoded_byte_data:
#         bits = bits + _int_to_bits(byte)

#     print(offset)
#     if offset != 0 and offset != b'':
#         bits = bits[offset:]

#     print('bits from inside func bytb D', bits)
#     return bits
