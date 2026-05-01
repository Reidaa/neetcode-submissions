class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        seen = set()
        re = []
        for word in strs:
            ordered = ''.join(sorted(word))
            seen.add(ordered)
            if ordered in seen:
                h[ordered] = [word] + h.get(ordered, [])
        for l in h:
            re.append(h[l])
        return re
        