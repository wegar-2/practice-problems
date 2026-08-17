

class Solution:
    """
    Tedious, suboptimal solution.
    """

    def convert(self, s: str, numRows: int) -> str:

        cols_num = 0
        sum_ = 0
        if numRows > 1:
            while sum_ < len(s):
                if cols_num % (numRows - 1) == 0:
                    sum_ += numRows
                else:
                    sum_ += 1
                cols_num += 1
        else:
            return s
        # print(f"{cols_num=}")
        # print(f"{sum_=}")

        d: dict[int, list[str]] = {
            i: ["" for _ in range(numRows)]
            for i in range(0, cols_num)
        }

        # write into zigzag
        sp = 0
        for j in range(cols_num):
            if (remainder := j % (numRows - 1)) == 0:
                for r in range(numRows):
                    if sp < len(s):
                        # print(f"{j=}, {r=}, {s[sp]=}")
                        d[j][r] = s[sp]
                        sp += 1
                    else:
                        break
            else:
                d[j][numRows - 1 - remainder] = s[sp]
                sp += 1

        # read from the zigzag
        out = []
        for r in range(numRows):
            for c in range(cols_num):
                out.append(d[c][r])
        return "".join(out)
