


def find_occ_positions2(nums: list[int]) -> list[int]:
    pass


if __name__ == "__main__":

    lst: list[int] = [1, 4, 2] # noqa

    # adding value at the end: .append
    lst.append(5)

    # inserting value at specific position: .insert
    lst.insert(1, 10)

    # popping value from the end: .pop() without arguments
    popped1 = lst.pop()

    # popping value from specific position: .pop() with argument
    popped2 = lst.pop(1)

    # finding first occurrence of a value
    # raises ValueError if the target value is not found
    pos_of_4 = lst.index(4)

    # removing specific value from the list: .remove()
    # note: only first occurrence is removed!
    lst = [1, 3, 6, 1, 4, 5, 90, 1]
    lst.remove(1)

    # reversing order of list elements in place
    lst.reverse()

    # counting # of occurrences of a specific value in the list
    count_of_1s = lst.count(1)

    # find index of first occurrence of a value in the list
    lst.index(90)
    lst.index(1234)

    # values: list[int] = [1, 10, 1, 56, 434, 1, 23, 3]
    # print(f"{find_occ_positions1(values, 1)=}")
