

def get_compressed_bits_map(tree):
    if not isinstance(tree, dict):
        return None

    bits_dict = {}

    def bits_finder(tree_, bits):
        if tree_['left'] is None and tree_['right'] is None:
            bits_dict[tree_['char']] = bits
        
        if isinstance(tree_['left'], dict):
            bits_finder(tree_=tree_['left'], bits=bits + '0')
        
        if isinstance(tree_['right'], dict):
            bits_finder(tree_=tree_['right'], bits=bits + '1')

    for key in tree:
        if tree[key]['left'] is None and tree[key]['right'] is None:
            bits_dict[tree[key]['char']] = '0'
            break
        bits_finder(tree[key], '')

    return bits_dict