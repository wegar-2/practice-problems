from typing import List


class Solution:

    def _retrieve_lens_and_text(self, s: str) -> tuple[list[int], str]:
        if (str_ := s[0:3].lstrip("0")) != "":
            num_of_words = int(str_)
        else:
            num_of_words = 0
        lens = []

        for i in range(1, num_of_words + 1):
            if (str_ := s[i * 4:i * 4 + 3].lstrip("0")) != "":
                lens.append(int(str_))
            else:
                lens.append(0)

        return lens, s[4*(num_of_words+1):]

    def encode(self, strs: List[str]) -> str:
        strs_num: int = len(strs)
        strs_lens: list[int] = [len(x) for x in strs]
        str_struct_encoding = (
            "_".join(
                [f"{strs_num:03}"] +
                [f"{l:03}" for l in strs_lens])
        )
        return str_struct_encoding + "_" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        lens, text = self._retrieve_lens_and_text(s)

        positions: list[int] = [0]
        for i in range(len(lens)):
            positions.append(positions[i] + lens[i])
        out = []
        for i in range(1, len(positions)):
            out.append(text[positions[i-1]:positions[i]])

        return out


if __name__ == "__main__":
    s = Solution()

    # s_enc = s.encode(["Hello", "", "World"])
    s_enc = s.encode(["", "qwertyy", ""])
    print(f"{s_enc=}")

    s_dec = s.decode(s_enc)
    print(f"{s_dec=}")

    from collections import deque

    dq = deque()
    dq.append()
    dq.popleft()