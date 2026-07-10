

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

# 5. retrieve binary representation of a number
def get_bin_rep(n: int) -> str:
    pass
