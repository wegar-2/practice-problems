

def is_power_of_two_logn(n: int) -> bool:
    if n <= 0:
        return False
    for i in range(n.bit_length() - 1):
        if (n >> i) & 1:
            return False
    if (n >> (n.bit_length() - 1)) & 1:
        return True
    return False


def is_power_of_two_o1(n: int) -> bool:
    if n > 0:
        return n & (n - 1) == 0
    return False


if __name__ == "__main__":
    for i in range(-32, 33):
        # print(f"is {i} a power of 2: {is_power_of_two_logn(i)}")
        print(f"is {i} a power of 2: {is_power_of_two_o1(i)}")
