

def _make_permutations(
        nums: list[int],
        start: int,
        perm: list[int],
        all_perms: list[int]
) -> list[list[int]]:
    pass




def make_permutations(n: int = 5):

    nums: list[int] = list(range(1, n + 1, 1))

    return _make_permutations(
        nums=nums,
        start=0,
        perm=[],
        all_perms=[]
    )
