import sys


def counter(arg: str):
    """counts and displays char types of a string"""
    print(f"The text contains {len(arg)} characters:")
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    digits = 0

    for char in arg:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            punct += 1

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Our main function, checks arguments, and pass to our counter function"""

    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
            counter(text)
        elif len(sys.argv) == 2:
            counter(sys.argv[1])
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
