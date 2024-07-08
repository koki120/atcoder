import sys
from typing import Iterable


def solver(input: Iterable[str]):
    numbers = [int(num_string) for num_string in next(input).split()]
    numbers.sort()

    return numbers[3]


if __name__ == "__main__":
    print(solver(sys.stdin))
