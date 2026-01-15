import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range"""

    bar_width = os.get_terminal_size().columns - 41  # rest of terminal
    len_lst = len(lst)

    for i, elem in enumerate(lst):
        percentage = int(i * 101 / len(lst))
        equals = int(bar_width * percentage / 100)
        spaces = bar_width - equals

        percentage_str = f"{percentage}"
        per_spaces = f"{' ' * (3 - len(percentage_str))}"
        print(f"{per_spaces}{percentage}%|", end='')
        print(f"{'=' * equals}>{' ' * spaces}| {i + 1}/{len_lst}", end='\r')
        yield elem
