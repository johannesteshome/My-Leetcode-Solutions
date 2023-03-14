class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        minLength = len(s)
        n = int(len(s) / 4)

        # for st in s:
        #     count[st] += 1
        
        correct= 0
        for cnt in count:
            if count[cnt] == n:
                correct += 1

        if correct == 4:
            return 0
        left = 0
        for right in range(len(s)):
            count[s[right]] -= 1
            if all(i <=n for i in list(count.values())):
                minLength = min(minLength, (right - left) + 1)
                while left<= right:
                    count[s[left]] += 1
                    left += 1
                    if all(i <=n for i in list(count.values())):
                        minLength = min(minLength, right - left + 1)
                    else:
                        break
                

        # right = 0
        # count[s[right]] -= 1
        # while left <= right:
        #     if all(i <=n for i in list(count.values())):
        #         print(count, left, right)
        #         minLength = min(minLength, (right - left) + 1)
        #         left += 1
        #         count[s[left-1]] += 1
        #     else: 
                
        #         if right < len(s) - 1:
        #             right += 1
        #             count[s[right]] -= 1
        #         else:
        #             if left < len(s):
        #                 left += 1
        #                 count[s[left]] += 1

        return minLength