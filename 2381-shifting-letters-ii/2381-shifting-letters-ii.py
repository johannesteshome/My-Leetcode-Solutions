class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = collections.Counter()
        for st, e, right in shifts:
            d[st] += 1 if right else -1
            if e+1 < n:
                d[e+1] += -1 if right else 1
        prefix = [0]
        ans = ''
        for i in range(n):
            cur = prefix[-1] + d[i]
            prefix.append(cur)
            ans += string.ascii_lowercase[(ord(s[i]) - ord('a') + cur) % 26]
        return ans