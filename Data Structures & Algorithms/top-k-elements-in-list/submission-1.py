import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        freqs = [[] for i in range(len(nums) + 1)]
        tops = []

        print(count)
        print(freqs)
        print(f"k: {k}")

        for key, v in count.items():
            freqs[v].append(key)
        # t = [c[0] for c in sorted(count.items(), key=lambda x: x[1], reverse=False)]
        # return t[k * -1:]

        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                tops.append(n)
                if len(tops) >= k:
                    return tops
    

        print(freqs)
        print(tops)
        return tops