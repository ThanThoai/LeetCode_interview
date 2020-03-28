class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            y = target - nums[i]
            if y in nums:
                x = nums.index(y)
                if x == i:
                    continue
                else:
                    return [i, x]
            else:
                continue