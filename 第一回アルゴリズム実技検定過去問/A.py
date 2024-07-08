from typing import Iterable
import sys


def check_number(c):
    return c in "0123456789"


def number_chr_to_number(c):
    return int(c) if check_number(c) else None


def string_to_number(num_string: str):
    return int(num_string)


def solver(input: Iterable[str]):
    S = next(input).strip()
    if not S:
        return "error"

    is_zero_top = True
    is_minus = S[0] == "-"
    num_string = ""

    # 0 check
    if S[0] == "0" and len(S) == 1:
        return 0

    # string to number
    for i, c in enumerate(S):
        if i == 0 and is_minus:
            continue

        if c == "0" and is_zero_top:
            continue
        elif check_number(c):
            is_zero_top = False
            num_string += c
        else:
            return "error"

    if not num_string:
        return "error"

    result = string_to_number(num_string) * 2
    return -result if is_minus else result


if __name__ == "__main__":
    print(solver(sys.stdin))
