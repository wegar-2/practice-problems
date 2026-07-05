
nl = [
    [1, 2, 3],
    ["q", "b", "p"]
]

flattened = [
    x
    for sl in nl
    for x in sl
]

print(f"{nl=}")
print(f"{flattened=}")
