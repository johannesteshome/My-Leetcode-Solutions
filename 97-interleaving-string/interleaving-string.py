class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if s1 == s2 == s3:
            return True

        memo = {}
        
        def backtrack(x, y, curr):
            # print(x, y, curr)
            state = (x,y,curr)
            sOne = False
            sTwo = False

            if state in memo:
                return memo[state]

            if curr == len(s3) - 1:
                if x == len(s1)-1 and y == len(s2) and s3[curr] == s1[x]:
                    return True
                if y == len(s2)-1 and x == len(s1) and s3[curr] == s2[y]:
                    return True

            if curr < len(s3):
                if x < len(s1) and s3[curr] == s1[x]:
                    sOne = backtrack(x+1, y, curr+1)
                    if sOne:
                        return True
                if y < len(s2) and s3[curr] == s2[y]:
                    sTwo = backtrack(x, y+1, curr+1)
                    if sTwo:
                        return True

            memo[state] = sOne or sTwo
            return memo[state]
        
        return backtrack(0,0,0)