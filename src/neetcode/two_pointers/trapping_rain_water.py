

def _next_gte(height: list[int]) -> list[int]:
    out: list[int] = [-1] * len(height)
    stack: list[tuple[int, int]] = []
    for i, x in enumerate(height):
        if not stack:
            stack.append((i, x))
        else:
            while stack and stack[-1][1] <= x:
                j, v = stack.pop()
                out[j] = i
            stack.append((i, x))
    return out


def trapping_rain_water(height: list[int]) -> int:

    area: int = 0

    if len(height) <= 2:
        return 0

    gte_height = _next_gte(height)

    gte_inv_height = _next_gte(height[::-1])
    gte_inv_height = [
        len(height) - 1 - j if j != -1 else -1 for j in gte_inv_height
    ][::-1]

    left = 0
    right = len(height) - 1

    # walk from left first
    while left < len(height):

        next_left = gte_height[left]
        if next_left == -1:
            break

        lvl = min(height[left], height[next_left])
        for i in range(left + 1, next_left):
            area += lvl - height[i]
            print(area)

        left = next_left

    # walk from the right
    while right > left:
        next_right = gte_inv_height[right]
        lvl = min(height[next_right], height[right])
        for i in range(next_right + 1, right):
            area += lvl - height[i]
            print(area)
        right = next_right

    return area


if __name__ == "__main__":
    # values = [5, 7, 2, 10, 3, 8, 32, 1, 9, 3]
    # res = _next_gte(values)
    # print(res)
    # for x, y in zip(values, res):
    #     print(f"{x} ---> {y}")

    heights = [1, 1, 2, 1, 3, 2, 5, 4, 3, 2, 9, 5, 3, 8, 1, 2, 3, 4, 3, 2, 1]
    #                   1     1     1  2  3     3  5     3  2  1
    # 8 + 6 + 8 = 22
    water = trapping_rain_water(heights)
    print(water)
