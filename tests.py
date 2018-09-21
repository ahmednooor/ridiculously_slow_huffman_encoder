import os, time

from huffman_encoder import (
    encode,
    decode,
    encode_file,
    decode_file
)

def test(input_file_path, output_dir, input_file_name):
    print('------------------------------------------------------------')
    print('TESTING FILE: "' + input_file_name + '"')
    print()
    t1 = time.time()
    is_encoded = encode_file(
        input_file_path,
        output_dir,
        'encoded_' + input_file_name + '.hc1'
    )
    if is_encoded:
        print('Encoding Succcessful!')

    
    is_decoded = decode_file(
        output_dir + 'encoded_' + input_file_name + '.hc1',
        output_dir,
        'decoded_' + input_file_name
    )
    if is_decoded:
        print('Decoding Succcessful!')
    t2 = time.time()
    
    with open(input_file_path, 'rb') as f:
        text_1 = f.read()
    with open(output_dir + 'decoded_' + input_file_name, 'rb') as f:
        text_2 = f.read()

    print()
    print('Tests:')
    print('1) funcs: [encode_file, decode_file]: \t' + str(text_1 == text_2))
    print('   Time Took (sec): \t' + str(t2 - t1))
    t3 = time.time()
    only_bytes_test = text_1 == decode(encode(text_1, single_output=True), single_output=True)
    t4 = time.time()
    print('2) funcs: [encode, decode]: \t\t' + str(only_bytes_test))
    print('   Time Took (sec): \t' + str(t4 - t3))
    
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
    print('Input File Size: \t' + str(os.path.getsize(input_file_path)) + ' bytes')
    print('Encoded File Size: \t' + str(os.path.getsize(output_dir + 'encoded_' + input_file_name + '.hc1')) + ' bytes')
    print('Percentage Compressed: \t' + '{0:.1f} %'.format(
        100 - ( ( os.path.getsize(output_dir + 'encoded_' + input_file_name + '.hc1') / os.path.getsize(input_file_path) )
        * 100 )
    ))
    print('------------------------------------------------------------')


def main():
    test('./test_files/sample_1.txt', './test_files/', 'sample_1.txt')
    test('./test_files/sample_2.png', './test_files/', 'sample_2.png')


if __name__ == '__main__':
    main()
