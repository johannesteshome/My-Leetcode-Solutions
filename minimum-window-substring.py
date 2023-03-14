class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # if len(t) == len(s):
        #     if s == t:
        #         return s
        #     else:
        #         return ""
        tCount = Counter(t)
        minString = s
        minStrings = []
        changed = False

        left = 0
        right = len(t) - 1


        sCount = Counter(s[left:right+1])

        while left <= right:
            # print(minString, left, right)
            if all(i in sCount and sCount[i] >= tCount[i] for i in tCount):
                if right-left+1 <= len(minString):
                    minString = s[left:right+1]
                    changed = True
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0: del sCount[s[left]]
                left += 1
            else:
                if right < len(s) - 1:
                    right += 1
                    sCount[s[right]] += 1
                else:
                    # print("here")
                    sCount[s[left]] -= 1
                    left += 1
        if not changed:
            return ""
        else:
            return minString