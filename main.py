# -*- coding: utf-8 -*-
"""Hennge code test solution by Oliver Vea.

Solution and a small pytest suite can be found on Github.
See: https://github.com/OliverVea/hennge-test.
"""

from typing import Iterator


def map_number(number: str) -> int:
    """Maps a string to an int.

    Args:
        number: The string to convert.

    Returns:
        The string converted to an integer.
        If the provided string is not numeric, 0 is returned instead.
    """
    if not number.isnumeric():
        return 0
    return int(number)


def read_number() -> int:
    """Reads a line from stdin, attempts to transform the value to an integer and returns it.

    Returns:
        The resulting integer.
    """
    line = input().strip()
    return map_number(line)


def read_positive_numbers(delimiter: str = ' ') -> Iterator[int]:
    """Reads a line from stdin and returns all positive integers from that line.

    If any substrings are not fully numeric, they are replaced by 0.
    This includes substrings with negative numbers.

    Args:
        delimiter: String used to separate numbers from stdin.

    Returns:
        An iterator of the integers that were found.
    """
    line = input()
    numbers = line.split(delimiter)
    return map(map_number, numbers)


def get_test_case_sum() -> int:
    """Gets the sum of a single test case by reading the next two lines from stdin.

    Returns:
        The sum of the values for the test case.
    """
    read_number()
    test_case_numbers = read_positive_numbers()
    return sum(test_case_numbers)


def main():
    """The main method of the solution."""
    test_case_count = read_number()

    # Is this cheating? It feels like cheating.
    sums = map(lambda _: get_test_case_sum(), range(test_case_count))
    sum_strings = map(str, sums)

    result = '\n'.join(sum_strings)

    # Only prints if result is not empty.
    if result:
        print(result)


if __name__ == "__main__":
    main()
