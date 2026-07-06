from typing import Optional


def make_subsets(
        values: list[int],
        all_subsets: list[list[int]],
        current_subset: Optional[list[int]] = None,
        start: int = 0,
) -> list[list[int]]:

    values = sorted(values)#[::-1]

    if current_subset is None:
        current_subset = []

    if start < len(values):
        all_subsets = make_subsets(
            values=values,
            all_subsets=all_subsets,
            start=start + 1,
            current_subset=current_subset
        )
        current_subset.append(values[start])
        all_subsets = make_subsets(
            values=values,
            all_subsets=all_subsets,
            start=start + 1,
            current_subset=current_subset
        )
        current_subset.pop()
        # all_subsets = make_subsets(
        #     values=values,
        #     all_subsets=all_subsets,
        #     start=start + 1,
        #     current_subset=current_subset
        # )
    else:
        all_subsets.append([x for x in current_subset])

    return all_subsets


if __name__ == "__main__":

    # list1 = [1, 2]
    # list2 = [list1, list1]
    # list1.pop()

    values = list(range(1, 5))
    all_subsets: list[list[int]] = []
    make_subsets(
        values=values,
        all_subsets=all_subsets,
        current_subset=[],
        start=0
    )
    print(f"{all_subsets=}")
