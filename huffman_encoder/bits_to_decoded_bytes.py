

def bits_to_decoded_bytes(bits, tree):
    if not isinstance(bits, str) or not isinstance(tree, dict):
        return None

    decoded_bytes = []
    cur_node = None
    
    for key in tree:
        cur_node = tree[key]

    for bit in bits:
        if bit == '0' and cur_node['left'] is not None:
            cur_node = cur_node['left']
        elif bit == '1' and cur_node['right'] is not None:
            cur_node = cur_node['right']
        
        if cur_node['left'] is None and cur_node['right'] is None:
            decoded_bytes.append(cur_node['char'])

            for key in tree:
                cur_node = tree[key]

    return b''.join(decoded_bytes)