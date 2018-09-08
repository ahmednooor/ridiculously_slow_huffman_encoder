import os

def read_byte_file(file_path):
    if not os.path.isfile(file_path):
        return None

    with open(file_path, 'rb') as test_file:
        byte_data = test_file.read()

    return byte_data
