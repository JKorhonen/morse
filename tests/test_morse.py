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

