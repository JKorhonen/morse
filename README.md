# Morse - English to Morse code converter
[![Build Status](https://travis-ci.org/JKorhonen/morse-coder.svg?branch=master)](https://travis-ci.org/JKorhonen/morse-coder)


A Simple library that provides basic facilities to convert English text to morse code or vice versa.

Currently, the library has some limitations how you can convert Morse code to English. We assume that Morse Code is 
structured following these rules:

Characters are separated from each other with a dot

There cannot be two dots in a row

`...---...` for Example is invalid string when we try to convert it back to English. Instead it should be represented 
as `....-.-.----.-.-.-...` and it translates `S.O.S`.

For testing purposes we provide simple CLI software that can be found in bin/morse-cli and it supports English to Morse 
conversion without restrictions. Morse to English contains the same restrictions as the library. Software will 
automatically detect if text is a morse code. User can specify characters for a dash and a dot.

## The example use of the library

```python
from morse import Morse

# Default values as example how to specify own dash and dot chars
converter = Morse(dot='.', dash='-')

text = "H.e.l.l.o.,.W.o.r.l.d"
morse = converter.english_to_morse(text)
print(morse)  # Output: ..-.-.-..-.-.-.-...-.-.-.-...-.-.----.-.-.---..--.-.-.-.--.-.-.----.-.-.-.-..-.-.-.-...-.-.--..
text2 = converter.morse_to_english(morse)
print(text2)  # Output: H.E.L.L.O.,.W.O.R.L.D
```
