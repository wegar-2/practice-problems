"""
Using else clause with for and while loops.

References:
    (1) https://www.w3schools.com/python/gloss_python_for_else.asp
    (2) https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement
"""


def _for_loop_else():
    print("FOR loop else clause")

    for x in range(4):
        print(f"{x=}")
    else:
        print("Exited the FOR loop elegantly")

    for i in range(1, 100):
        print(f"{i=}")
        if i % 12 == 0:
            print("breaking out of the FOR loop")
            break
    else:
        print("Graciously exited FOR loop")

def _while_loop_else():
    print("WHILE loop else clause")

    x = 0
    while x < 5:
        print(f"{x=}")
        x += 1
    else:
        print("Exited the WHILE loop elegantly")

    i = 1
    while i < 100:
        print(f"{i=}")
        if i % 12 == 0:
            print("breaking out of the WHILE loop")
            break
        i += 1
    else:
        print("Graciously exited WHILE loop")


def main():
    _for_loop_else()
    _while_loop_else()


if __name__ == "__main__":
    main()
