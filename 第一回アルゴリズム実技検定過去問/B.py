import sys
from typing import Iterable


def solver(input: Iterable[str]):
    result = []
    N = int(next(input).strip())
    pre_earning = int(next(input).strip())
    for _ in range(N - 1):
        earning = int(next(input).strip())
        if earning == pre_earning:
            result.append("stay")
        elif earning < pre_earning:
            result.append(f"down {pre_earning - earning}")
        else:
            result.append(f"up {earning - pre_earning}")
        pre_earning = earning
    return result


if __name__ == "__main__":
    result = solver(sys.stdin)
    for s in result:
        print(s)
