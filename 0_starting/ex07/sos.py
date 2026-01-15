import sys


def get_morse(msg: str, err: str):
    """returns morse code if exists"""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    morse_parts = []
    for char in msg:
        if char.upper() in NESTED_MORSE:
            morse_parts.append(NESTED_MORSE[char.upper()])
        else:
            raise AssertionError(err)
    morse_msg = "".join(morse_parts)
    print(morse_msg)


def main():
    """Main function to encode text to Morse code"""

    err = "the arguments are bad"

    try:
        if len(sys.argv) != 2:
            raise AssertionError(err)
        get_morse(sys.argv[1], err)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
