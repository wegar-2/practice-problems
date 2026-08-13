from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stck: list[str | int] = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operand2: int = int(stck.pop())
                operand1: int = int(stck.pop())
                if token == "+":
                    stck.append(operand1 + operand2)
                elif token == "-":
                    stck.append(operand1 - operand2)
                elif token == "*":
                    stck.append(operand1 * operand2)
                else:
                    res = operand1 / operand2
                    if res > 0:
                        res = math.floor(res)
                    else:
                        res = math.ceil(res)
                    stck.append(res)
            else:
                stck.append(token)

        return int(stck[0])
