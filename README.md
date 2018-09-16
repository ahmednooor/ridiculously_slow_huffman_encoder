# ridiculously_slow_huffman_encoder
not so slow now (not so fast either)
- can do all files (hopefully)
- text files compress well, while other files sometimes don't (sometimes expand instead)

![Screenshot](https://raw.githubusercontent.com/ahmednooor/ridiculously_slow_huffman_encoder/master/assets/screenshot.png)

### running the app in gui mode
> clone this repo

> double click `gui_main.pyw` to run the app

### using as a package
> `python 3+` is a must (that rhymes)

> copy the `huffman_encoder` dir to your proj dir and then,

```python
from huffman_encoder import (
    encode,
    decode,
    encode_file,
    decode_file
)
```
> check `tests.py` to get the hang of it

> start from `interface.py` in `huffman_encoder/` if you want to read the source

### build executable
- only for windows

> replace python dir path with your's

> run `make_exec.bat` in cmd

> resultant `.exe` will be in `dist/` delete `build/` after completion

### meta
> do whatever you want

> author: ahmed noor
