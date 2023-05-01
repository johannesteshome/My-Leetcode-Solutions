class Solution:
    def firstUniqChar(self, s: str) -> int:
        occ = [0] * len(s)
        chars = defaultdict(int)

        for i in range(len(s)):
            chars[s[i]] += 1
        
        for i in range(len(occ)):
            if chars[s[i]] == 1:
                return i

        return -1