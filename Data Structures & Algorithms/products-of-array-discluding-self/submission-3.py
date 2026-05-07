import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i, _ in enumerate(nums):
            t = []
            if i == 0:
                t = nums[1:]
            elif i == (len(nums) - 1):
                t = nums[:-1]
            else:
                t = nums[i+1:] + nums[:i]

            res.append(math.prod(t))

        return res
        