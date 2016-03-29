# xorlenfind

I wrote this script to help find the key length in a repeating XOR cipher. 

A CTF I recently competed in had a challenge involving a repeating XOR cipher. The common [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) method for finding the key length looked boring, so I took a different approach and wrote this script.

This method makes the assumption that both the plaintext message and key are composed entirely by printable ASCII, defined by python's `string` module's `printable` variable (`string.printable`). It searches each key length less than the ciphertext's length, finding which printable characters at each key index will always yield printable ASCII when XORed with the ciphertext as the key repeats. If that doesn't make sense, look at the code.

It works best with long ciphertexts, rating the most likely length candidate as the one yielding the least amount of possible values.

### Usage
```
python lenfind.py <hex data>
```

`<hex data>` being the ciphertext encoded to hex. Note that hex values such as `0x8` should be passed as two characters instead of one, in this case `08`.
