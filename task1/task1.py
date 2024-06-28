import sys
from collections import deque


def get_path(n: int, m: int) -> list[int]:
    lst = ''.join(map(str, list(range(1, n + 1))))

    array = deque(lst)
    res = list(array[0])
    array.rotate(-(m - 1))
    while array[0] != lst[0]:
        res.append(array[0])
        array.rotate(-(m - 1))
    return res


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    path = get_path(n, m)
    print(*path)