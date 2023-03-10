class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(fs, i):
            # print(fs)
            if len(fs) >= 2:
                if fs[-2] - fs[-1] != 1:
                    return
                elif fs[-2] - fs[-1] == 1 and i == len(s):
                    return True
            
            for j in range(i+1, len(s)+1):
                v = backtrack(fs + [int(s[i:j])], j)
                # print(v)
                if v:
                    return True
        
        a = backtrack([], 0)
        if a:
            return True
        return False