import os
from pathlib import Path

def write_text_file(dir_path, file_name, text):
    if not os.path.exists(dir_path):
        return None

    dir_path = Path(dir_path)
    file_path = dir_path / file_name

    with open(file_path, 'w') as output_file:
        output_file.write(text)

    return True
