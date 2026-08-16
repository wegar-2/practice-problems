

def count_bits(n: int):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        out = [0, 1]
        for k in range(2, n + 1):
            out.append(1 + out[k - 2 ** (k.bit_length() - 1)])

    return out
