from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_ = 0
        for x in details:
            s = x[11:13].lstrip("0")
            if not s:
                s = "0"
            count_ += int(s) > 60
        return count_
