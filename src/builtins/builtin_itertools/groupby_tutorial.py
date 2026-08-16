from itertools import groupby


if __name__ == "__main__":
    lst = [1, 0, 1, 1, 0, 1, 1, 0, 1]
    res = groupby(lst)
    print(f"{res=}")
    for x, y in res:
        print(f"{x}: {(y)}")
