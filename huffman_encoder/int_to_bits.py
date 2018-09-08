

def int_to_bits(int_num):
    if not isinstance(int_num, int):
        return None

    bits = ''

    while int_num > 1:
        bits = str(int_num % 2) + bits
        int_num = int_num // 2

    bits = str(int_num % 2) + bits
    bits = bits[1:]

    return bits