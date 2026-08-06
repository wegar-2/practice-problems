# 100000.....0000
# n zeros

def is_power_of_two_v1(x: int) -> bool:
    for i in range(x.bit_length()):
        if i <= x.bit_length() - 2:
            if x >> i & 1:
                return False
        else:
            if not x >> i & 1:
                return False
    return True


def is_power_of_two_v2(x: int) -> bool:
     return 2**(x.bit_length() - 1) == x & (2**x.bit_length() - 1)


if __name__ == "__main__":
    # print(f"{is_power_of_two_v1(4)=}")
    for i in range(100):
        print(f"{i:03} ===> {is_power_of_two_v2(i)=}")
