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

## Morse API
Declaration of methods that Morse class provides

### Character tools
```python
def get_char(self, code: str) -> (str, None):
    """
    Get char from code
    :param code: Morse code in external format
    :return: English char
    """
```

```python
def get_code(self, char: str) -> (str, None):
    """
    Get morse code from char
    :param char: English char
    :return: Morse code in external format
    """
```

### Conversion tools
```python
def morse_to_english(self, code: str) -> str:
    """
    Convert Morse Code to English text or throw ValueError if not possible
    :param code: Morse code in external format
    :return: English text
    """
```

```python
def english_to_morse(self, text: str) -> str:
    """
    Convert English text to Morse code or throw ValueError if character doesn't have morse code representation
    :param text: English text to be translated
    :return: Morse code
    """
```

### Comparision tools
```python
def is_morse_code(self, code: str) -> bool:
    """
    Check if given code morse code or not
    :param code: Text to be analyzed
    :return: True if represent morse code, othervise false
    """
```