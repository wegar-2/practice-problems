

def daily_temperatures(temperatures: list[int]) -> list[int]:

    result = [0] * len(temperatures)

    stck: list[tuple[int, int]] = []

    for i, x in enumerate(temperatures):
        if stck:
            while stck and stck[-1][1] < x:
                j, _ = stck.pop()
                result[j] = i - j
        stck.append((i, x))

    return result


if __name__ == "__main__":
    res = daily_temperatures([30,38,30,36,35,40,28])
    print(res)