import regex


class Morse:
    """A Class that contains information and facilities about morse codes"""
    _codes = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '@': '.--.-.',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
    }

    _dash = '-'
    _dot = '.'

    def __init__(self, dash: str = '-', dot: str = '.') -> None:
        """
        A Constructor
        :param dash: How to print dash
        :param dot: How to print dot
        """
        self.dash = dash
        self.dot = dot

    def get_code(self, char: str) -> (str, None):
        """
        Get the morse cad that represent given character
        :param char: English letter, digit or symbol that have morse code
        :return: string that represent a code
        """
        if char.upper() in self.__class__._codes:
            code = self.__class__._codes[char.upper()]
            code = code.replace(self.__class__._dot, self.dot)
            code = code.replace(self.__class__._dash, self.dash)
            return code
        return None

    def get_char(self, code: str) -> (str, None):
        """
        Get character from given morse code
        :param morse:
        :return:
        """
        code = code.replace(self.dot, self.__class__._dot)
        code = code.replace(self.dash, self.__class__._dash)
        for char, code_i in self.__class__._codes.items():
            if code == code_i:
                return char
        return None

    def english_to_morse(self, text_input: str) -> str:
        """
        Convert english text to morse code.
        :param text_input: text to be translated
        :return: string that contains morse code
        """
        # Return string
        morse = ""
        for i in range(0, len(text_input)):
            code = self.get_code(text_input[i])
            if code is not None:
                morse += code
            else:
                raise ValueError("Invalid character")
        return morse

    def morse_to_english(self, text_input: str) -> str:
        """
        Convert morse code with next assumptions:
        1. Between characters there is one dot (.-.-.-)
        2. There cannot be two dots in row
        :param text_input: morse code
        :return: plain english text
        """
        # Convert input to internal representation
        if self.__class__._dash != self.dash:
            text_input = text_input.replace(self.dash, self.__class__._dash)
        if self.__class__._dot != self.dot:
            text_input = text_input.replace(self.dot, self.__class__._dot)

        # Check if dot
        if text_input == '.-.-.-':
            return '.'
        # build regex string
        re_chars = "|".join(self.__class__._codes.values())
        re_chars = re_chars.replace('|.-.-.-', '')  # Remove dot
        re_str = "^(?:(?P<char>" + re_chars + ")(.-.-.-))*(?P<last_char>" + re_chars + ")$"
        re_str = re_str.replace(r"|)", r")")
        re_str = re_str.replace(r".", r"\.")
        parser = regex.compile(re_str)
        # Check that given input is valid
        result = parser.match(text_input)
        if result is None:
            raise ValueError("Invalid morse code")
        # Start translate
        text = "."
        chars = map(lambda x: self.get_char(x), result.captures("char"))
        text = text.join(chars)
        if text != "":
            text += "." + self.get_char(result.captures("last_char")[0])
        else:
            text = self.get_char(result.captures("last_char")[0])
        return text
