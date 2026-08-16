

def make_permutations(n: int = 4) -> list[list[int]]:

    out: list[list[int]] = []
    nums: list[int] = list(range(1, n + 1, 1))

    def _make_permutations(current: list[int], used: list[bool]):
        if len(current) == n:
            out.append([x for x in current])
        else:
            for i in range(n):
                if not used[i]:
                    current.append(nums[i])
                    used[i] = True
                    _make_permutations(current, used)

                    current.pop()
                    used[i] = False

    _make_permutations([], [False for _ in range(n)])

    return out


if __name__ == "__main__":

    res = make_permutations(n=4)
    print(f"{len(res)=}")
    print(f"{res=}")

