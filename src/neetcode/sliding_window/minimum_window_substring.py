from collections import defaultdict


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(s) == 0:
            return ""

        # min_len_str: str = ""
        mls_left, mls_right = 0, 0

        counts_t: dict[str, int] = {}
        for l in t:
            if l not in counts_t:
                counts_t[l] = 1
            else:
                counts_t[l] += 1

        met_conditions: dict[str, bool] = {l: False for l in counts_t}
        met_conditions_count: int = 0
        counts: defaultdict[str, int] = defaultdict(int)

        left = 0
        for right, x in enumerate(s):

            if x in counts_t:
                counts[x] += 1
                if counts[x] >= counts_t[x] and not met_conditions[x]:
                    met_conditions[x] = True
                    met_conditions_count += 1

            # move left pointer forward as far as possible
            while met_conditions_count == len(counts_t):

                if mls_right - mls_left == 0:
                    mls_left, mls_right = left, right + 1
                elif right - left + 1 < mls_right - mls_left:
                    mls_left, mls_right = left, right + 1

                popped: str = s[left]
                left += 1
                if popped in counts_t:
                    counts[popped] -= 1
                    if counts[popped] < counts_t[popped]:
                        if met_conditions[popped]:
                            met_conditions[popped] = False
                            met_conditions_count -= 1

        return s[mls_left:mls_right]


if __name__ == "__main__":

    solution = Solution()

    s = "OUZODYXAZV"
    t = "XYZ"

    print(f"{solution.minWindow(s, t)=}")
