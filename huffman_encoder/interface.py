from .get_frequencies import get_frequencies
from .make_tree import make_tree
from .get_bits_map import get_bits_map
from .text_to_bits import text_to_bits
from .bits_to_bytes import bits_to_bytes
from .freq_to_bytes import freq_to_bytes
from .comb_freq_data_bytes import comb_freq_data_bytes
from .sep_freq_data_bytes import sep_freq_data_bytes
from .bytes_to_bits import bytes_to_bits
from .bits_to_text import bits_to_text
from .read_text_file import read_text_file
from .write_byte_file import write_byte_file
from .read_byte_file import read_byte_file
from .write_text_file import write_text_file

# TODO return meaningful stuff rather than none in case of errors or raise exceptions
# TODO just raise exceptions instead or give some err code to now where the prob is
# TODO make it compatible with all files rather than just text (read bytes instead of text)
# TODO provide a gui wrapper

def encode(text, single_output=False):
    freq_map = get_frequencies(text)
    tree = make_tree(freq_map)
    bits_map = get_bits_map(tree)
    bits = text_to_bits(bits_map, text)
    encoded_data_bytes = bits_to_bytes(bits)
    freq_bytes = freq_to_bytes(freq_map)
    final_output_bytes = comb_freq_data_bytes(freq_bytes, encoded_data_bytes)

    # print('--ENCODE LOCALS')
    # print('--ENCODE LOCALS')
    # print(freq_map, '\n',  tree, '\n', bits, '\n', \
    #     encoded_data_bytes, '\n', freq_bytes, '\n', final_output_bytes)
    # print('--ENCODE LOCALS END')

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


def encode_file(text_file_path, output_dir, out_file_name):
    text = read_text_file(text_file_path)
    encoded_output = encode(text)
    
    if encoded_output is None:
        return False
    
    encoded_output_bytes = encoded_output['final_output_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, encoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True


def decode(total_byte_data, single_output=False):
    freq_map, encoded_data_bytes = sep_freq_data_bytes(total_byte_data)
    encoded_bits = bytes_to_bits(encoded_data_bytes)
    tree = make_tree(freq_map)
    text = bits_to_text(encoded_bits, tree)

    # print('--DECODE LOCALS')
    # print('--DECODE LOCALS')
    # print(freq_map, '\n', tree, '\n', encoded_bits, '\n', encoded_data_bytes, '\n', \
    #     total_byte_data.split(b'\x00\x00\x00')[0], text)
    # print('--DECODE LOCALS END')

    if None in [freq_map, encoded_data_bytes, encoded_bits, tree, text]:
        return None

    if single_output is True:
        return text

    return {'freq_map': freq_map, 
            'encoded_data_bytes': encoded_data_bytes, 
            'encoded_bits': encoded_bits, 
            'tree': tree, 
            'text': text}



def decode_file(encoded_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(encoded_file_path)
    decoded_output = decode(byte_data)

    if decoded_output is None:
        return False

    decoded_output_text = decoded_output['text']
    is_out_file_written = write_text_file(output_dir, out_file_name, decoded_output_text)

    if is_out_file_written is None:
        return False

    return True
