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
        Get morse code from char
        :param char: English char
        :return: Morse code in external format
        """
        return self.__convert_to_external(self.__get_code(char))

    def __get_code(self, char: str) -> (str, None):
        """
        Get morse code from char
        :param char: English char
        :return: Morse code in internal format
        """
        if char.upper() in self.__class__._codes:
            return self.__class__._codes[char.upper()]
        return None

    def get_char(self, code: str) -> (str, None):
        """
        Get char from code
        :param code: Morse code in external format
        :return: English char
        """
        code = self.__convert_to_internal(code)
        return self.__get_char(code)

    def __get_char(self, code: str) -> (str, None):
        """
        Get char from code that is in internal format
        :param code: Morse code in internal format
        :return: English char
        """
        for char, code_i in self.__class__._codes.items():
            if code == code_i:
                return char
        return None

    def english_to_morse(self, text: str) -> str:
        """
        Convert English text to Morse code or throw ValueError if character doesn't have morse code representation
        :param text: English text to be translated
        :return: Morse code
        """
        # Remove whitespace
        pattern = regex.compile(r"\s+")
        text = regex.sub(pattern, '', text)
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
        Convert Morse Code to English text or throw ValueError if not possible
        :param code: Morse code in external format
        :return: English text
        """
        # Convert input to internal representation
        code = self.__convert_to_internal(code)

        # Check if the input is a dot
        if code == self.__get_code('.'):
            return '.'

        # Parse input string with regex
        parser = regex.compile(self.__create_validation_string())
        result = parser.match(code)
        # Check that morse code is valid and we can parse it
        if result is None:
            raise ValueError("Invalid morse code")
        # Start translate
        chars = map(lambda x: self.__get_char(x), result.captures("char"))
        text = ".".join(chars)
        if text != "":
            text += "." + self.__get_char(result.captures("last_char")[0])
        else:
            text = self.__get_char(result.captures("last_char")[0])
        return text

    def is_morse_code(self, code: str) -> bool:
        """
        Check if given code morse code or not
        :param code: Text to be analyzed
        :return: True if represent morse code, othervise false
        """
        regex_str = "^[{}{}]+$".format(regex.escape(self.dot), regex.escape(self.dash))
        pattern = regex.compile(regex_str)
        if regex.match(pattern, code):
            return True
        return False

    def __create_validation_string(self) -> str:
        """
        Create validation regex string
        :return: Return validation regex string
        """
        dot = self.__get_code('.')
        chars = "|".join(self.__class__._codes.values())
        chars = chars.replace('|{}'.format(dot), '')  # remove the dot from
        regex_str = "^(?:(?P<char>" + chars + ")(" + dot +  "))*(?P<last_char>" + chars + ")$"
        regex_str = regex_str.replace(".", r"\.")
        return regex_str

    def __convert_to_internal(self, code: str) -> str:
        """
        Convert a code string to internal format
        dash='-', dot='.'
        :param code: Morse code in external format
        :return: Morse code in internal format
        """
        if self.dot != self.__class__._dot:
            code = code.replace(self.dot, self.__class__._dot)
        if self.dash != self.__class__._dash:
            code = code.replace(self.dash, self.__class__._dash)
        return code

    def __convert_to_external(self, code: str) -> str:
        """
        Convert a morse code to external format
        :param code: Morse code in internal format
        :return: Morse code in external format
        """
        if self.dot != self.__class__._dot:
            code = code.replace(self.__class__._dot, self.dot)
        if self.dash != self.__class__._dash:
            code = code.replace(self.__class__._dash, self.dash)
        return code
