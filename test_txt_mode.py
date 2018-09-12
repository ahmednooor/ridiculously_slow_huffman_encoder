import os

from huffman_encoder import (
    encode_txt,
    decode_txt,
    encode_txt_file,
    decode_txt_file
)

def main():
    is_encoded = encode_txt_file('./test_files/sample_txt.txt', './test_files/', 'encoded_txt.hc1')
    if is_encoded:
        print('Encoding Succcessful!')

    is_decoded = decode_txt_file('./test_files/encoded_txt.hc1', './test_files/', 'decoded_txt.txt')
    if is_decoded:
        print('Decoding Succcessful!')

    with open('./test_files/sample_txt.txt', 'r') as f:
        text_1 = f.read()
    with open('./test_files/decoded_txt.txt', 'r') as f:
        text_2 = f.read()

    # srsly, don't look at this code
    print()
    print('Tests:')
    print('1) funcs: [encode_txt_file, decode_txt_file]: \t' + str(text_1 == text_2))
    print('2) funcs: [encode_txt, decode_txt]: \t\t' + \
          str(text_1 == decode_txt(encode_txt(text_1, single_output=True), single_output=True)))
    
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
    print('Text File Size: \t' + str(os.path.getsize('./test_files/sample_txt.txt')) + ' bytes')
    print('Encoded File Size: \t' + str(os.path.getsize('./test_files/encoded_txt.hc1')) + ' bytes')
    print('Percentage Compressed: \t' + '{0:.1f} %'.format(
        100 - ( ( os.path.getsize('./test_files/encoded_txt.hc1') / os.path.getsize('./test_files/sample_txt.txt') )
        * 100 )
    ))

if __name__ == '__main__':
    main()
