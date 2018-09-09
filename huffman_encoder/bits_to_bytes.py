from .helpers import int_to_bytes

def bits_to_bytes(bits):
    if not isinstance(bits, str):
        return None

    bits = '1' + bits
    int_num = int(bits, 2)
    bytes_str = int_to_bytes(int_num)
    
    return bytes_str


# def _bits_to_int(bits):
#     # print(bits, 'tttttttttt')
#     bits = bits[::-1]
#     int_num = 0
#     bit_place = 1

#     for bit in bits:
#         if bit == '1':
#             int_num += bit_place
#         bit_place *= 2

#     return int_num

# def bits_to_bytes(bits):
#     if not isinstance(bits, str):
#         return None

#     print('bits from inside func btby E', bits)
#     offset = 0
#     while len(bits) % 8 != 0:
#         bits = '1' + bits
#         offset += 1
#     print('bits from inside fu  EEEEEEE', bits)
    
#     bits_len = len(bits)
#     index = 0
#     bytes_arr = []

#     while index + 8 <= bits_len:
#         bits_to_conv = bits[index:index + 8]
#         int_num = int(bits_to_conv, 2)
#         bytes_arr.append(int_to_bytes(int_num))
#         index += 8
    
#     bytes_arr.append(b'\x00')
#     bytes_arr.append(int_to_bytes(offset))
    
#     print('bytes from inside func btby E', b''.join(bytes_arr))
#     return b''.join(bytes_arr)
