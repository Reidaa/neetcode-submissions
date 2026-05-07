import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        t = [c[0] for c in sorted(count.items(), key=lambda x: x[1], reverse=False)]
        return t[k * -1:]