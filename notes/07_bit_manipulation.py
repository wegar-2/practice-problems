

x = 5
print(f"{x=}")
print(f"{x=:0b}")

# 1. XOR
x = 12 # 1100
y = 10 # 1010
print(f"{x=:0b}")
print(f"{y=:0b}")
print(f"{(x^y)=:04b}")

# 2. bit-wise AND
print(f"{(x & y)=:04b}")

# 3. bit-wise OR
print(f"{(x | y)=:04b}")

# 4. retrieve i-th smallest bit from binary rep of number n
def get_bit(n: int, i: int):
    return (n >> i) & 1

x = 5
print(f"{x=}")
print(f"{x=:04b}")

for i in range(3):
    print(f"{i=}: {get_bit(x, i)=}")


# 5. retrieve binary representation of a number
def get_bin_rep(n: int) -> str:
    bits = []
    for i in range(n.bit_length()):
        bits.append(get_bit(n, i))
    return "".join(bits[::-1])

# 6. set the i-th bit of a number to 1
n = 17
print(f"{n=}")
print(f"{n=:0b}")
n |= (1 << 2) # if i-th bit from right is 1 - it remains 1; if it is 0, it beomes 1
print(f"{n=:0b}")

# 7. clear the i-th bit
n &= ~(1 << 2)
print(f"{n=:0b}")

z = 5
print(f"{z=:05b}")
z &= ~(1 << 2)
print(f"{z=:05b}")


# 8. flipping the i-th bit
x = 0b10101
print(f"{x=:06b}")
x ^= (1 << 2)
print(f"{x=:06b}")
x ^= (1 << 2)
print(f"{x=:06b}")

