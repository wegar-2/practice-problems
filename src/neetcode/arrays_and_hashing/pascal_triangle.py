from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []

        for i in range(1, numRows + 1):
            if i == 1:
                out.append([1])
            elif i == 2:
                out.append([1, 1])
            else:
                row = [1]
                for j in range(len(out[-1]) - 1):
                    row.append(out[-1][j] + out[-1][j+1])
                row.append(1)
                out.append(row)
        return out
