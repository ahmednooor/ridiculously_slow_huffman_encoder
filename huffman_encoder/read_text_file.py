import os

def read_text_file(file_path):
    if not os.path.isfile(file_path):
        return None

    text = r''''''
    
    with open(file_path, 'r') as input_file:
        text = input_file.read()

    return text