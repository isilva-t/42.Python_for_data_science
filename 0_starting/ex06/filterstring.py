import sys
from ft_filter import ft_filter


def main():
    """Main function to filter words by length"""

    err = "the arguments are bad"
    try:
        if len(sys.argv) == 3:
            try:
                n = int(sys.argv[2])
            except ValueError:
                raise AssertionError(err)
            words = sys.argv[1].split()
            filtered = ft_filter(lambda word: len(word) > n, words)
            print(filtered)
        else:
            raise AssertionError(err)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
