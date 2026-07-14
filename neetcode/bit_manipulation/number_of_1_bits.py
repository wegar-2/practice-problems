

def number_of_1_bits(n: int):
    out = 0
    for i in range(n.bit_length()):
        out += (n >> i) & 1
    return out

if __name__ == "__main__":
    res = number_of_1_bits(5)
    print(res)