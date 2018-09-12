from .get_frequencies import get_frequencies
from .make_tree import make_tree
from .get_bits_map import get_bits_map
from .text_to_bits import text_to_bits
from .bits_to_bytes import bits_to_bytes
from .freq_to_bytes import freq_to_bytes
from .comb_freq_data_bytes import comb_freq_data_bytes
from .sep_freq_data_bytes import sep_freq_data_bytes
from .bytes_to_bits import bytes_to_bits
from .bits_to_decoded_text import bits_to_decoded_text
from .read_text_file import read_text_file
from .write_byte_file import write_byte_file
from .read_byte_file import read_byte_file
from .write_text_file import write_text_file

# imports related to bin mode
from .get_freq_bin import get_freq_bin
from .freq_to_bytes_bin import freq_to_bytes_bin
from .sep_freq_data_bytes_bin import sep_freq_data_bytes_bin
from .bits_to_decoded_bytes_bin import bits_to_decoded_bytes_bin


# -d -impr TODO make it compatible with all files rather than just text (read bytes instead of text)
# TODO return meaningful stuff rather than none in case of errors or raise exceptions
# TODO just raise exceptions instead or give some err code to now where the prob is
# TODO provide a gui wrapper

def encode_txt(text, single_output=False):
    freq_map = get_frequencies(text)
    tree = make_tree(freq_map)
    bits_map = get_bits_map(tree)
    bits = text_to_bits(bits_map, text)
    encoded_data_bytes = bits_to_bytes(bits)
    freq_bytes = freq_to_bytes(freq_map)
    final_output_bytes = comb_freq_data_bytes(freq_bytes, encoded_data_bytes)

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


def encode_txt_file(text_file_path, output_dir, out_file_name):
    text = read_text_file(text_file_path)
    encoded_output = encode_txt(text)
    
    if encoded_output is None:
        return False
    
    encoded_output_bytes = encoded_output['final_output_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, encoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True


def decode_txt(total_byte_data, single_output=False):
    freq_map, encoded_data_bytes = sep_freq_data_bytes(total_byte_data)
    encoded_bits = bytes_to_bits(encoded_data_bytes)
    tree = make_tree(freq_map)
    decoded_text = bits_to_decoded_text(encoded_bits, tree)

    if None in [freq_map, encoded_data_bytes, encoded_bits, tree, decoded_text]:
        return None

    if single_output is True:
        return decoded_text

    return {'freq_map': freq_map, 
            'encoded_data_bytes': encoded_data_bytes, 
            'encoded_bits': encoded_bits, 
            'tree': tree, 
            'decoded_text': decoded_text}


def decode_txt_file(encoded_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(encoded_file_path)
    decoded_output = decode_txt(byte_data)

    if decoded_output is None:
        return False

    decoded_output_text = decoded_output['decoded_text']
    is_out_file_written = write_text_file(output_dir, out_file_name, decoded_output_text)

    if is_out_file_written is None:
        return False

    return True


def encode_bin(byte_data, single_output=False):
    byte_data = [bytes([byte]) for byte in byte_data]

    freq_map = get_freq_bin(byte_data)
    tree = make_tree(freq_map)
    bits_map = get_bits_map(tree)
    bits = text_to_bits(bits_map, byte_data)
    encoded_data_bytes = bits_to_bytes(bits)
    freq_bytes = freq_to_bytes_bin(freq_map)
    final_output_bytes = comb_freq_data_bytes(freq_bytes, encoded_data_bytes)

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


def encode_bin_file(bin_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(bin_file_path)
    encoded_output = encode_bin(byte_data)
    
    if encoded_output is None:
        return False
    
    encoded_output_bytes = encoded_output['final_output_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, encoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True


def decode_bin(total_byte_data, single_output=False):
    freq_map, encoded_data_bytes = sep_freq_data_bytes_bin(total_byte_data)
    encoded_bits = bytes_to_bits(encoded_data_bytes)
    tree = make_tree(freq_map)
    decoded_bytes = bits_to_decoded_bytes_bin(encoded_bits, tree)

    if None in [freq_map, encoded_data_bytes, encoded_bits, tree, decoded_bytes]:
        return None

    if single_output is True:
        return decoded_bytes

    return {'freq_map': freq_map, 
            'encoded_data_bytes': encoded_data_bytes, 
            'encoded_bits': encoded_bits, 
            'tree': tree, 
            'decoded_bytes': decoded_bytes}


def decode_bin_file(encoded_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(encoded_file_path)
    decoded_output = decode_bin(byte_data)

    if decoded_output is None:
        return False

    decoded_output_bytes = decoded_output['decoded_bytes']
    is_out_file_written = write_byte_file(output_dir, out_file_name, decoded_output_bytes)

    if is_out_file_written is None:
        return False

    return True
