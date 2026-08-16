

def next_greater_element(values: list[int]) -> list[int]:

    mstack: list[tuple[int, int]] = []
    nge: list[int] = [-1 for _ in values]

    for i, x in enumerate(values):
        while mstack:
            j, y = mstack[-1]
            if y < x:
                mstack.pop()
                nge[j] = i
            else:
                break

        mstack.append((i, x))

    return nge


if __name__ == "__main__":

    values = [10, 5, 4, 3, 7, 11, 7, 10, 5]
    print(f"{next_greater_element(values)=}")
