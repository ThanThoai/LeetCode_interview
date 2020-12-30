"""
https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
"""
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        # print(count)
        for s, e in requests:
            # print(s, e)
            count[s] += 1
            count[e + 1] -= 1
            # print(count)
        # print(count)
        for i in range(1, n):
            count[i] += count[i - 1]
        # print(count)
        result = sum(i * j for i, j in zip(sorted(count[:-1]), sorted(nums)))
        return int(result % (10 ** 9 + 7))



if __name__ == "__main__":

    sol = Solution()
    print(sol.maxSumRangeQuery(nums = [1, 2, 3, 4, 5], requests=[[1, 3], [0, 1]]))