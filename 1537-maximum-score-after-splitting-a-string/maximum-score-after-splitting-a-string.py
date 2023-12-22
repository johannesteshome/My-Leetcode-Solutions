class Solution:
    def maxScore(self, s: str) -> int:
        Max = float("-inf")
        count = Counter(s)
        ones = count["1"]
        zeros = count["0"]
        left = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                left += 1
            if s[i] == "1":
                ones -= 1
            Max = max(Max, left + ones)
        
        return Max


        