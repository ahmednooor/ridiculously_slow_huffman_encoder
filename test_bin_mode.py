import os

from huffman_encoder import (
    encode_bin,
    decode_bin,
    encode_bin_file,
    decode_bin_file
)

def main():
    is_encoded = encode_bin_file('./test_files/sample_bin.png', './test_files/', 'encoded_bin.hc1')
    if is_encoded:
        print('Encoding Succcessful!')

    is_decoded = decode_bin_file('./test_files/encoded_bin.hc1', './test_files/', 'decoded_bin.png')
    if is_decoded:
        print('Decoding Succcessful!')

    with open('./test_files/sample_bin.png', 'rb') as f:
        text_1 = f.read()
    with open('./test_files/decoded_bin.png', 'rb') as f:
        text_2 = f.read()

    # srsly, don't look at this code
    print()
    print('Tests:')
    print('1) funcs: [encode_bin_file, decode_bin_file]: \t' + str(text_1 == text_2))
    print('2) funcs: [encode_bin, decode_bin]: \t\t' + \
          str(text_1 == decode_bin(encode_bin(text_1, single_output=True), single_output=True)))
    
    i = 0
    text_1_len = len(text_1)
    text_2_len = len(text_2)
    while i < text_1_len and i < text_2_len:
        if text_1[i] != text_2[i]:
            print('ERR: mismaatched at char: ', i + 1)
            break
        i += 1


    print()
    print('Stats:')
    print('Input File Size: \t' + str(os.path.getsize('./test_files/sample_bin.png')) + ' bytes')
    print('Encoded File Size: \t' + str(os.path.getsize('./test_files/encoded_bin.hc1')) + ' bytes')
    print('Percentage Compressed: \t' + '{0:.1f} %'.format(
        100 - ( ( os.path.getsize('./test_files/encoded_bin.hc1') / os.path.getsize('./test_files/sample_bin.png') )
        * 100 )
    ))

if __name__ == '__main__':
    main()
