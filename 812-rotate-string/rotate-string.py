class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0 
        j = len(goal) - 1

        for _ in range(len(goal)):
            if goal[i:] + goal[:(j+1)%len(goal)] == s:
                return True
            
            i += 1
            j += 1
        
        return False