from functools import reduce
from collections import Counter


if __name__ == "__main__":

    def add(x, y):
        print(f"{x=}")
        print(f"{y=}")
        return x + y

    res = reduce(
        add,
        [2, 3, 4],
        1
    )
    print(f"{res=}")

    lst = [0, 5, 3]
    lst.remove(3)

    set1 = {"a", "b"}
    set1.add("c")
    set1.remove("a")
