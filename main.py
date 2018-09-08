import os

from huffman_encoder import encode, decode, encode_file, decode_file

def main():
    is_encoded = encode_file('./test_files/test.txt', './test_files/', 'encoded.hc1')
    if is_encoded:
        print('Encoding Succcessful!')

    is_decoded = decode_file('./test_files/encoded.hc1', './test_files/', 'decoded.txt')
    if is_decoded:
        print('Decoding Succcessful!')

    with open('./test_files/test.txt', 'r') as f:
        text_1 = f.read()
    with open('./test_files/decoded.txt', 'r') as f:
        text_2 = f.read()

    # srsly, don't look at this code
    print()
    print('Tests:')
    print('1) funcs: [encode_file, decode_file]: \t' + str(text_1 == text_2))
    print('2) funcs: [encode, decode]: \t\t' + \
          str(text_1 == decode(encode(text_1, only_bytes=True), only_text=True)))
    
    print()
    print('Stats:')
    print('Text File Size: \t' + str(os.path.getsize('./test_files/test.txt')) + ' bytes')
    print('Encoded File Size: \t' + str(os.path.getsize('./test_files/encoded.hc1')) + ' bytes')
    print('Percentage Compressed: \t' + str(
        100 - ( ( os.path.getsize('./test_files/encoded.hc1') / os.path.getsize('./test_files/test.txt') )
        * 100 )
    ) + ' %')

if __name__ == '__main__':
    main()
