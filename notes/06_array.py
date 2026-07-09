import random
from array import array


if __name__ == "__main__":

    ar = array("i", [0] * 10)

    for i in range(10):
        ar[i] = random.randint(1, 101)

    print(f"{ar=}")
