class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        Max = max(nums)

        left = 0
        right = 0
        n = len(nums)
        answer = 0
        dic = defaultdict(int)
        dic[nums[0]] = 1

        while right < n:
            # print(dic, left, right)
            
            if Max in dic and dic[Max] >= k:
                answer += (n - right)
                dic[nums[left]] -= 1
                left += 1
            
            else:
                right += 1
                if right < n:
                    dic[nums[right]] += 1

        
        return answer
        