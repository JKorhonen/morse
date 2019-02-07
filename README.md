# Morse - English to Morse code converter
Simple library that provides basic facilities to convert English text to morse code or vice versa.

Currently the library have few limitations how you can convert Morse code to English. We assume that Morse Code is 
structured following these rules:
1. After every character, there is a dot
2. There cannot be two dots in a row

Example `...---...` this is invalid string when we try to convert it back to English. Instead it should be represented
as `....-.-.----.-.-.-...` and it translates `S.O.S`.

For testing purposes we provide simple CLI software that can be found in `bin/morse-cli` and it supports English to 
Morse conversion without restrictions and it will automatically remove white space. Morse to English conversion must
follow rules mentioned earlier or it will give you error message.

Software will automatically detect if text is morse code and user can specify letters for dash and dot that are used
in morse code.

## Example use of library
Library provides few endpoints for users and you can see them in work in next example
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

## Example use of software
To use example CLI that demonstrates how morse library works: 
```
# morse <input_file> <output_file>
morse-cli morse.txt english.txt
```

```
morse.txt
....-.-.----.-.-.-...
```

```
english.txt
S.O.S
```

## Installation instructions
TODO