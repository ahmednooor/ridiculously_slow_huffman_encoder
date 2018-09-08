

def bits_to_int(bits):
    if not isinstance(bits, str):
        return None

    bits = '1' + bits
    bits = bits[::-1]
    int_num = 0
    bit_place = 1

    for bit in bits:
        if bit == '1':
            int_num += bit_place
        bit_place *= 2

    return int_num