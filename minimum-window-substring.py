class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if the length of t is greater than length of s then its invalid
        if len(t) > len(s):
            return ""
        
        # count the number of occurences of the characters in t
        tCount = Counter(t)
        minString = s
        # to check if the algorithm found a minimum substring
        changed = False

        left = 0
        right = len(t) - 1

        # count the number of occurences of characters in the sliding window
        sCount = Counter(s[left:right+1])

        while left <= right:
            # if all characters in t are present in the window and their frequencies is also the same or greater than in t
            if all(i in sCount and sCount[i] >= tCount[i] for i in tCount):
                # if it finds the minimum substring it updates it
                if right-left+1 <= len(minString):
                    minString = s[left:right+1]
                    changed = True
                # if min substring is found it shrinks the window
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0: del sCount[s[left]]
                left += 1
            else:
                # if not it expands the window but by being cautious by not incrementing the value of right not to extend the length of s which results in list index out of range
                if right < len(s) - 1:
                    right += 1
                    sCount[s[right]] += 1
                # if the right pointer reaches its maximum limit we simply shrink the window until its  end
                else:
                    # print("here")
                    sCount[s[left]] -= 1
                    left += 1
        # if minimum substring is not found
        if not changed:
            return ""
        else:
            return minString