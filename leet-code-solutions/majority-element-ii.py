class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        count = Counter(nums)
        answer = []

        for c in count:
            if count[c] > n:
                answer.append(c)
        
        return answer