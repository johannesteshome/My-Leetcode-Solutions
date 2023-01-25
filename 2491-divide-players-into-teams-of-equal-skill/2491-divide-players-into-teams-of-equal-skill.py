class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        Sum = skill[left] + skill[right]
        sums = []
        sums.append((skill[left], skill[right]))
        
        left+=1
        right-=1
        while left < right:
            if skill[left] + skill[right] == Sum:
                sums.append((skill[left], skill[right]))  
            else:
                return -1
            left += 1
            right -= 1
        result = 0
        for s in sums:
            result = result + (s[0] * s[1])
            
        return result
            
            