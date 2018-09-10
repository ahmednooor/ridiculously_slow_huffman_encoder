# ridiculously_slow_huffman_encoder
not so slow now (not so fast either)
- can do all files (hopefully)
- text files compress well, while other files sometimes don't (sometimes expand)
- although bin mode can compress text files as well, but better use text mode for text files (saves a couple bytes)

### usage
> `python 3+` is a must (that rhymes)

> copy the `huffman_encoder` dir to your proj dir and then,

```python
from huffman_encoder import (
    encode_txt,
    decode_txt,
    encode_txt_file,
    decode_txt_file,
    encode_bin,
    decode_bin,
    encode_bin_file,
    decode_bin_file
)
```
> check `test_bin_mode.py` and `test_txt_mode.py` to get the hang of it

> start from `interface.py` in `huffman_encoder/` if you want to read the source

### meta
> do whatever you want
> author: ahmed noor
