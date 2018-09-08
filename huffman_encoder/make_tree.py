

def make_tree(tree):
    if not isinstance(tree, dict):
        return None

    tree = { x: { 'freq': tree[x], 'char': x, 'left': None, 'right': None } for x in tree }

    while len(tree) != 1:
        min_1 = None
        min_2 = None
        min_1_node = None
        min_2_node = None

        for key in tree:
            if min_1 is None:
                min_1 = key
            if tree[key]['freq'] < tree[min_1]['freq']:
                min_1 = key
        
        min_1_node = tree[min_1]
        del tree[min_1]
        
        for key in tree:
            if min_2 is None:
                min_2 = key
            if tree[key]['freq'] < tree[min_2]['freq']:
                min_2 = key
        
        min_2_node = tree[min_2]
        del tree[min_2]

        tree[min_1 + min_2] = {
            'freq': min_1_node['freq'] + min_2_node['freq'],
            'char': min_1 + min_2,
            'left': min_1_node,
            'right': min_2_node
        }

    return tree
