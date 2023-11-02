class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(start, end, s):
            if start == 0 and end == 0:
                ans.append(s)
                return
            
            if start == 0 and end != 0:
                backtrack(start, end-1, s+')')
            elif start == end:
                backtrack(start-1, end, s+'(')
            elif start < end:
                backtrack(start-1, end, s+'(')
                backtrack(start, end-1, s+')')
        
        backtrack(n,n,'')
        return ans
        