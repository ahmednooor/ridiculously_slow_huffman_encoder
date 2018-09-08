

def int_to_bytes(x):
    '''taken from https://stackoverflow.com/a/30375198'''
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    '''taken from https://stackoverflow.com/a/30375198'''
    return int.from_bytes(xbytes, 'big')