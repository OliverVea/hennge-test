

#  We want you to calculate the sum of squares of given integers, excluding any negatives.
#  The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
#  Each of the test cases will consist of a line with an integer X (0 < X <= 100), 
# followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
#  For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.

# Note: There should be no output until all the input has been received.
# Note 2: Do not put blank lines between test cases solutions.
# Note 3: Take input from standard input, and output to standard output.

from typing import Iterator


def map_number(number: str) -> int:
    """Maps a string to an int.

    Args:
        number: The string to convert.

    Returns:
        The string converted to an integer. If the provided string is not numeric, 0 is returned instead.
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

    If any substrings are not fully numeric, they are replaced by 0, including substrings with negative numbers.

    Args:
        delimiter: String used to separate numbers from stdin.

    Returns:
        An iterator of the integers that were found.
    """
    line = input()
    numbers = line.split(delimiter)
    a = map(map_number, numbers)
    return a


def get_test_case_sum(iteration: int) -> int:
    """Gets the sum of a single test case by reading the next two lines from stdin.

    Returns:
        The sum of the values for the test case.
    """
    test_case_number_count = read_number()
    test_case_numbers = read_positive_numbers()
    return sum(test_case_numbers)


def main():
    test_case_count = read_number()

    # Is this cheating? It feels like cheating.
    sums = map(get_test_case_sum, range(test_case_count))
    sum_strings = map(str, sums)

    result = '\n'.join(sum_strings)

    # Only prints if result is not empty.
    if result:
        print(result)


if __name__ == "__main__":
    main()
