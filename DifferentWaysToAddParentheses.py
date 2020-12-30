"""
https://leetcode.com/problems/different-ways-to-add-parentheses/
"""

from typing import List

class Solution:


    def diffWaysToCompute(self, inputs: str) -> List[int]:
        output = []
        for i, s in enumerate(inputs):
            if  s in ["+", "-", "*"]:
                str_1 = inputs[:i]
                str_2 = inputs[i + 1:]
                print(str_1)
                list_str_1 = self.diffWaysToCompute(str_1)
                list_str_2 = self.diffWaysToCompute(str_2)
                print(list_str_1, list_str_2)
                for s_1 in list_str_1:
                    for s_2 in list_str_2:
                        if s == "+":
                            output.append(int(s_1)  + int(s_2))
                        elif s == "-":
                            output.append(int(s_1) - int(s_2))
                        else:
                            output.append(int(s_1) * int(s_2))
        if not len(output):
            output.append(int(inputs)) 
        return output



if __name__ == "__main__":

    sol = Solution()
    print(sol.diffWaysToCompute(inputs = "21*3-4*5"))