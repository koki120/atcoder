from typing import Iterable
import sys
import copy


def check_number(c):
    return c in "0123456789"


def string_to_number(num_string: str):
    return int(num_string)


def solver(input: Iterable[str]):
    S = next(input).strip()
    if not S:
        return "error"

    # 符号判定かつ符号を取り除く
    is_minus = S[0] == "-"
    if is_minus:
        S = S[1:]

    # 不要なゼロを取り除く
    S_len = len(S)
    is_top = True
    S_old = copy.deepcopy(S)
    for i in range(S_len):
        if S_old[i] == "0" and i != S_len - 1 and is_top:
            S = S_old[i:]
        else:
            is_top = False

    # 数字にアルファベットが入ってないかチェック
    num_string = ""
    for i, c in enumerate(S):
        if check_number(c):
            num_string += c
        else:
            return "error"

    result = string_to_number(num_string) * 2
    return -result if is_minus else result


if __name__ == "__main__":
    print(solver(sys.stdin))
