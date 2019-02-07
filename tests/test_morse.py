import pytest
from morse import Morse


def test_get_char_valid_args():
    converter = Morse()

    char1 = converter.get_char('.-.-.-')
    char2 = converter.get_char('.')
    char3 = converter.get_char('-')

    assert char1 == '.'
    assert char2 == 'E'
    assert char3 == 'T'


def test_get_char_invalid_args():
    converter = Morse()

    char1 = converter.get_char('ABC')
    char2 = converter.get_char('.-.-.-.-.-')
    char3 = converter.get_char('')

    assert char1 is None
    assert char2 is None
    assert char3 is None


def test_get_char_with_custom_dot_and_dash():
    converter = Morse(dot='0', dash='1')

    char = converter.get_char('010101')
    assert char == '.'


def test_get_code_valid_args():
    converter = Morse()

    morse1 = converter.get_code('.')
    morse2 = converter.get_code('a')
    morse3 = converter.get_code('Z')

    assert morse1 == '.-.-.-'
    assert morse2 == '.-'
    assert morse3 == '--..'


def test_get_code_invalid_args():
    converter = Morse()

    morse1 = converter.get_code('Ö')
    morse2 = converter.get_code('#')
    morse3 = converter.get_code('}')

    assert morse1 is None
    assert morse2 is None
    assert morse3 is None


def test_get_code_with_custom_dot_and_dash():
    converter = Morse(dot='Up', dash='Down')

    morse1 = converter.get_code('.')
    morse2 = converter.get_code('a')
    morse3 = converter.get_code('Z')

    assert morse1 == 'UpDownUpDownUpDown'
    assert morse2 == 'UpDown'
    assert morse3 == 'DownDownUpUp'


def test_english_to_morse():
    converter = Morse()

    morse1 = converter.english_to_morse("SOS")
    morse2 = converter.english_to_morse("Hello,World")

    assert morse1 == '...---...'
    assert morse2 == '......-...-..-----..--.-----.-..-..-..'


def test_english_to_morse_with_cstom_dot_and_dash():
    converter = Morse(dot='0', dash='1')

    morse1 = converter.english_to_morse("SOS")

    assert morse1 == "000111000"


def test_english_to_morse_invalid_args():
    converter = Morse()

    with pytest.raises(ValueError):
        converter.english_to_morse("Eipäotaselvää...")


def test_morse_to_english_valid_args():
    converter = Morse()

    morse1 = converter.english_to_morse("S.O.S")
    morse2 = converter.english_to_morse(".")
    morse3 = converter.english_to_morse("A")
    morse4 = converter.english_to_morse("H.E.L.L.O.W.O.R.L.D")

    text1 = converter.morse_to_english(morse1)
    text2 = converter.morse_to_english(morse2)
    text3 = converter.morse_to_english(morse3)
    text4 = converter.morse_to_english(morse4)

    assert "S.O.S" == text1
    assert "." == text2
    assert "A" == text3
    assert "H.E.L.L.O.W.O.R.L.D" == text4


def test_morse_to_english_valid_args_with_custom_dot_and_dash():
    converter = Morse(dot="CAT", dash="DOG")

    morse1 = converter.english_to_morse("S.O.S")
    morse2 = converter.english_to_morse(".")
    morse3 = converter.english_to_morse("A")
    morse4 = converter.english_to_morse("H.E.L.L.O.W.O.R.L.D")

    text1 = converter.morse_to_english(morse1)
    text2 = converter.morse_to_english(morse2)
    text3 = converter.morse_to_english(morse3)
    text4 = converter.morse_to_english(morse4)

    assert "S.O.S" == text1
    assert "." == text2
    assert "A" == text3
    assert "H.E.L.L.O.W.O.R.L.D" == text4


def test_morse_to_english_invalid_args():
    converter = Morse()

    with pytest.raises(ValueError):
        converter.morse_to_english(converter.english_to_morse("A.B."))

    with pytest.raises(ValueError):
        converter.morse_to_english(converter.english_to_morse(".A"))

    with pytest.raises(ValueError):
        converter.morse_to_english(converter.english_to_morse("A..A"))
