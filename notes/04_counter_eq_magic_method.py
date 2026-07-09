from collections import Counter


if __name__ == "__main__":
    a = "zxcx"
    b = "xxcz"

    if Counter(a) == Counter(b):
        print("same counts of letters")
