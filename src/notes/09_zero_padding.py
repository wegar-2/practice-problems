

if __name__ == "__main__":

    x = 11

    # using f-string
    print(f"{x=:06}")
    print(f"{x=:04}")

    # using str.zfill method
    print(f"{str(x).zfill(6)=}")
