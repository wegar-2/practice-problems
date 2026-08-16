

def insert_sort(values: list[int]) -> list[int]:
    for i in range(1, len(values), 1):

        val = values[i]
        j = i - 1

        while j >= 0 and values[j] > val:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = val

    return values


if __name__ == "__main__":

    values = [19, 4, 1, 10, 6, 23, 33, 7, 23, 34, 909, 65, 101]
    res = insert_sort(values)
    print(f"{res=}")
