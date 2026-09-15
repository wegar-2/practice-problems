from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0

        for i, x in enumerate(chars):
            if i == 0:
                cc = x
                cc_count = 1
                if len(chars) == 1:
                    chars[write] = cc
                    write += 1
            else:
                if x != cc:
                    if cc_count == 1:
                        chars[write] = cc
                        write += 1
                    else:
                        for l in cc + str(cc_count):
                            chars[write] = l
                            write += 1
                    cc, cc_count = x, 1
                    if i == len(chars) - 1:
                        chars[write] = cc
                        write += 1;
                else:
                    cc_count += 1
                    if i == len(chars) - 1:
                        if cc_count == 1:
                            chars[write] = cc
                            write += 1
                        else:
                            for l in cc + str(cc_count):
                                chars[write] = l
                                write += 1
        return write
