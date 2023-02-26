class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits) == 1:
            return 1
        
        content = defaultdict(int)
        
        left = 0
        right = 1
        
        content[fruits[left]] += 1
        content[fruits[right]] += 1
        Max = 2
        
        right += 1
        
        while right < len(fruits):
            if fruits[right] in content:
                content[fruits[right]] += 1
                Max = max(Max, right-left+1)
                right += 1
            elif fruits[right] not in content and len(content) == 2:
                if content[fruits[left]] == 1:
                    del content[fruits[left]]
                else:
                    content[fruits[left]] -= 1
                left += 1
            elif fruits[right] not in content and len(content) != 2:
                content[fruits[right]] += 1
                Max = max(Max, right-left+1)
                right += 1
                
        return Max
                
                
            