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
        return self.__convert_to_external(self.__get_code(char))

    def __get_code(self, char: str) -> (str, None):
        if char.upper() in self.__class__._codes:
            return self.__class__._codes[char.upper()]
        return None

    def get_char(self, code: str) -> (str, None):
        """
        Get character from given morse code
        :param code:
        :return:
        """
        code = self.__convert_to_internal(code)
        return self.__get_char(code)

    def __get_char(self, code: str) -> (str, None):
        for char, code_i in self.__class__._codes.items():
            if code == code_i:
                return char
        return None

    def english_to_morse(self, text: str) -> str:
        """
        Convert english text to morse code.
        :param text: text to be translated
        :return: string that contains morse code
        """
        # Return string
        morse = ""
        for i in range(0, len(text)):
            code = self.get_code(text[i])
            if code is not None:
                morse += code
            else:
                raise ValueError("Invalid character")
        return morse

    def morse_to_english(self, code: str) -> str:
        """
        Convert morse code with next assumptions:
        1. Between characters there is one dot (.-.-.-)
        2. There cannot be two dots in row
        :param code: morse code
        :return: plain english text
        """
        # Convert input to internal representation
        code = self.__convert_to_internal(code)

        # Check if the input is a dot
        if code == self.__get_code('.'):
            return '.'

        # Parse input string with regex
        parser = regex.compile(self.__create_validation_string())
        result = parser.match(code)

        if result is None:
            raise ValueError("Invalid morse code")
        # Start translate
        text = "."
        chars = map(lambda x: self.__get_char(x), result.captures("char"))
        text = text.join(chars)
        if text != "":
            text += "." + self.__get_char(result.captures("last_char")[0])
        else:
            text = self.__get_char(result.captures("last_char")[0])
        return text

    def __create_validation_string(self) -> str:
        dot = self.__get_code('.')
        chars = "|".join(self.__class__._codes.values())
        chars = chars.replace('|{}'.format(dot), '')  # remove the dot from
        regex_str = "^(?:(?P<char>" + chars + ")(" + dot +  "))*(?P<last_char>" + chars + ")$"
        regex_str = regex_str.replace(".", r"\.")
        return regex_str

    def __convert_to_internal(self, code: str) -> str:
        if self.dot != self.__class__._dot:
            code = code.replace(self.dot, self.__class__._dot)
        if self.dash != self.__class__._dash:
            code = code.replace(self.dash, self.__class__._dash)
        return code

    def __convert_to_external(self, code: str) -> str:
        if self.dot != self.__class__._dot:
            code = code.replace(self.__class__._dot, self.dot)
        if self.dash != self.__class__._dash:
            code = code.replace(self.__class__._dash, self.dash)
        return code
