from .get_frequencies import get_frequencies
from .make_tree import make_tree
from .get_bits import get_bits
from .text_to_bits import text_to_bits
from .bits_to_int import bits_to_int
from .int_to_bits import int_to_bits
from .bits_to_text import bits_to_text
from .freq_int_from_bytes import freq_int_from_bytes
from .freq_int_to_bytes import freq_int_to_bytes
from .read_text_file import read_text_file
from .write_byte_file import write_byte_file
from .read_byte_file import read_byte_file
from .write_text_file import write_text_file


def encode(text, only_bytes=False):
    freq_map = get_frequencies(text)
    tree = make_tree(freq_map)
    bits_map = get_bits(tree)
    bits = text_to_bits(bits_map, text)
    int_num = bits_to_int(bits)
    byte_data = freq_int_to_bytes(freq_map, int_num)

    if None in [freq_map, tree, bits_map, bits, int_num, byte_data]:
        if only_bytes:
            return None
        return None, None, None, None, None, None

    if only_bytes:
        return byte_data

    return freq_map, tree, bits_map, bits, int_num, byte_data


def encode_file(text_file_path, output_dir, out_file_name):
    text = read_text_file(text_file_path)
    freq_map, tree, bits_map, bits, int_num, byte_data = encode(text)
    is_out_file_written = write_byte_file(output_dir, out_file_name, byte_data)

    if None in [text, freq_map, tree, bits_map, bits, int_num, is_out_file_written]:
        return False

    return True


def decode(byte_data, only_text=False):
    freq_map, int_num = freq_int_from_bytes(byte_data)
    bits_from_num = int_to_bits(int_num)
    tree = make_tree(freq_map)
    text = bits_to_text(bits_from_num, tree)

    if None in [freq_map, int_num, bits_from_num, tree, text]:
        if only_text:
            return None
        return None, None, None, None, None

    if only_text:
        return text
    
    return freq_map, int_num, bits_from_num, tree, text


def decode_file(encoded_file_path, output_dir, out_file_name):
    byte_data = read_byte_file(encoded_file_path)
    freq_map, int_num, bits_from_num, tree, text = decode(byte_data)
    is_out_file_written = write_text_file(output_dir, out_file_name, text)

    if None in [freq_map, int_num, tree, bits_from_num, tree, text, is_out_file_written]:
        return False

    return True
