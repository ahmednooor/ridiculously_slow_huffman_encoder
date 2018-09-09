# ridiculously_slow_huffman_encoder
ok, not so slow now
- can only do text files

### usage
> `python 3+` is a must (that rhymes)

> copy the `huffman_encoder` dir to your proj dir and then,

```python
from huffman_encoder import (
    encode, # takes text and returns bytes to write to a file
    decode, # takes encoded bytes and returns text
    encode_file, # takes text file path, output dir path and output file name
    decode_file # takes encoded file path, output dir path and output file name
)
```
> check `main.py` to get the hang of it

> start from `interface.py` in `huffman_encoder/` if you want to read the source

### meta
> do whatever you want
