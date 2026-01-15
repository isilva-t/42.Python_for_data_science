import sys


def whatis(arg_one: str):

    try:
        if (int(arg_one) % 2 == 0):
            print("I'm Even.")
        elif (int(arg_one) % 2):
            print("I'm Odd.")
    except Exception:
        raise AssertionError("argument is not an integer")


def main():

    try:
        if len(sys.argv) == 1:
            pass
        elif len(sys.argv) == 2:
            arg = str(sys.argv[1])
            whatis(arg)
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
