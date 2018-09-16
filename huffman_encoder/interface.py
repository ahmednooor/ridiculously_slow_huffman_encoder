from .get_freq_map import get_freq_map
from .make_tree import make_tree
from .get_compressed_bits_map import get_compressed_bits_map
from .bits_to_decoded_bytes import bits_to_decoded_bytes
from .freq_to_bytes import freq_to_bytes
from .sep_freq_data_bytes import sep_freq_data_bytes
from .compressed_bits_to_bytes import compressed_bits_to_bytes
from .comb_freq_data_bytes import comb_freq_data_bytes
from .encoded_bytes_to_bits import encoded_bytes_to_bits
from .write_byte_file import write_byte_file
from .read_byte_file import read_byte_file
from .input_bytes_to_compressed_bits import input_bytes_to_compressed_bits


# TODO return meaningful stuff like err codes or exceptions rather than None in case of errors
# -d TODO make it compatible with all files rather than just text (read bytes instead of text)
# -d TODO provide a gui wrapper

_ENCODING_YIELDS = {}

def encode(byte_data, single_output=False):
    byte_data = [bytes([byte]) for byte in byte_data]

    freq_map = get_freq_map(byte_data)
    tree = make_tree(freq_map)
    bits_map = get_compressed_bits_map(tree)
    bits = input_bytes_to_compressed_bits(bits_map, byte_data)
    encoded_data_bytes = compressed_bits_to_bytes(bits)
    freq_bytes = freq_to_bytes(freq_map)
    final_output_bytes = comb_freq_data_bytes(freq_bytes, encoded_data_bytes)

    # _ENCODING_YIELDS['freq_map'] = freq_map
    # _ENCODING_YIELDS['tree'] = tree
    # _ENCODING_YIELDS['bits_map'] = bits_map
    # _ENCODING_YIELDS['bits'] = bits
    # _ENCODING_YIELDS['encoded_data_bytes'] = encoded_data_bytes
    # _ENCODING_YIELDS['freq_bytes'] = freq_bytes
    # _ENCODING_YIELDS['final_output_bytes'] = final_output_bytes
    
    if None in [freq_map, tree, bits_map, bits, \
               encoded_data_bytes, freq_bytes, final_output_bytes]:
        return None

    if single_output is True:
        return final_output_bytes

    return {'freq_map': freq_map, 
            'tree': tree, 
            'bits_map': bits_map, 
            'bits': bits, 
            'encoded_data_bytes': encoded_data_bytes, 
            'freq_bytes': freq_bytes, 
            'final_output_bytes': final_output_bytes}


def encode_file(bin_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(bin_file_path)
    encoded_output = encode(byte_data)
    
    if encoded_output is None:
        return False
    
    encoded_output_bytes = encoded_output['final_output_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, encoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True


def decode(total_byte_data, single_output=False):
    freq_map, encoded_data_bytes = sep_freq_data_bytes(total_byte_data)
    bits = encoded_bytes_to_bits(encoded_data_bytes)
    tree = make_tree(freq_map)
    decoded_bytes = bits_to_decoded_bytes(bits, tree)

    # print(freq_map == _ENCODING_YIELDS['freq_map'])
    # print(tree == _ENCODING_YIELDS['tree'])
    # print(bits == _ENCODING_YIELDS['bits'])
    # print(encoded_data_bytes == _ENCODING_YIELDS['encoded_data_bytes'])
    
    if None in [freq_map, encoded_data_bytes, bits, tree, decoded_bytes]:
        return None

    if single_output is True:
        return decoded_bytes

    return {'freq_map': freq_map, 
            'encoded_data_bytes': encoded_data_bytes, 
            'bits': bits, 
            'tree': tree, 
            'decoded_bytes': decoded_bytes}


def decode_file(encoded_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(encoded_file_path)
    decoded_output = decode(byte_data)

    if decoded_output is None:
        return False

    decoded_output_bytes = decoded_output['decoded_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, decoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True
