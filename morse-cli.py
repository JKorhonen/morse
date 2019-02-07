import regex

from morse import Morse


def main():
    dot = r'\.'
    dash = '-'

    print("MORSE-CLI VERSION 1.0.0\n")
    input_file_name = input("Input file: ")
    output_file_name = input("Output file: ")

    print("Processing input file\n")
    data = ""
    # Let's remove whitespace
    with open(input_file_name, "r") as fh:
        # Read all data into string
        input_data = fh.read().replace('\n', '')
        # Remove whitespace
        pattern = regex.compile(r"\s+")
        input_data = regex.sub(pattern, '', input_data)
        # Check if file is morse code and create output file
        morse_pattern = regex.compile(r"["+dot+dash+"]+$")
        converter = Morse(dot=dot, dash=dash)
        if regex.match(morse_pattern, input_data):
            print("Input type is Morse code")
            try:
                data = converter.morse_to_english(input_data)
            except ValueError:
                print("Invalid morse code, cannot create output file")
        else:
            print("Input type is English text")
            try:
                data = converter.english_to_morse(input_data)
            except ValueError:
                print("Cannot convert text into morse code, check supported chars")
    with open(output_file_name, "w") as fh:
        # Write data to file
        fh.write(data)
    print("DONE\n")


if __name__ == '__main__':
    main()
