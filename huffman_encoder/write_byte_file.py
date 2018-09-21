import os
from pathlib import Path

def write_byte_file(dir_path, file_name, byte_data):
    if not os.path.exists(dir_path):
        return None

    dir_path = Path(dir_path)
    file_path = dir_path / file_name

    with open(str(file_path), 'wb') as output_file:
        output_file.write(byte_data)

    return True
