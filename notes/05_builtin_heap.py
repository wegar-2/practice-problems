import heapq


if __name__ == "__main__":

    nums = [10, 4, 2, 1, 8, 5, 32, 1, 323, 901]
    l = []

    print("pushing to (min-)heap")
    for x in nums:
        heapq.heappush(l, x)

    print(f"{heapq.nlargest(3, l)=}")
    print(f"{l=}")

    print("popping from heap")
    for i in range(len(nums)):
        print(f"{i}-th pop: {heapq.heappop(l)}")
