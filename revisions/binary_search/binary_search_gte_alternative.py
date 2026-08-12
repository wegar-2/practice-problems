from typing import Optional


def binary_search_gte(
        nums: list[int],
        target: int,
        left: int = 0,
        right: Optional[int] = None
):

    
    if right is None:
        right = len(nums) - 1
