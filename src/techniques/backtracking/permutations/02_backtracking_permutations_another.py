

def permutations(n: int = 5) -> list[list[int]]:

    out: list[list[int]] = []
    current: list[int] = []
    used: list[bool] = [False for _ in range(n)]
    nums: list[int] = [i for i in range(1, n+1, 1)]

    def _recurse():
        if len(current) == n:
            out.append([x for x in current])
        else:
            for i in range(n):
                if not used[i]:
                    current.append(nums[i])
                    used[i] = True
                    _recurse()

                    current.pop()
                    used[i] = False

    _recurse()

    return out


if __name__ == "__main__":
    res = permutations(3)
    print(f"{len(res)=}")
    print(f"{res=}")
