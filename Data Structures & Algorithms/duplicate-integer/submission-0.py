class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d: dict = {}
        for num in nums:
            k = str(num)
            if k not in d:
                d[k] = False
            if d[k] == True:
                return True
            d[k] = True
        return False