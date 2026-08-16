# ordinary python dict keeps the order of its keys fixed

import random

random.seed(1234)

d = {
    i: random.randint(1, 100) for i in range(1, 6, 1)
}
for k, v in d.items():
    print(f"{k}: {v}")

d[3] = 123_456_789
for k, v in d.items():
    print(f"{k}: {v}")
