class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 1:
            if len(arr[0]) == len(set(arr[0])):
                return len(arr[0])
            else:
                return 0
        
        Max = 0
        
        def backtrack(i, string):
            nonlocal Max

            if i >= len(arr):
                return
            
            if string == "":
                setString = set(arr[i])
                if len(arr[i]) == len(setString):
                    string += arr[i]
                    Max = max(Max, len(string))
                else:
                    return
            else:
                setString = set(string)
                setString2 = set(arr[i])
                if len(arr[i]) == len(setString2):
                    if setString.isdisjoint(setString2):
                        string += arr[i]
                        Max = max(Max, len(string))
                    else:
                        return
                else:
                    return
            
            for j in range(i+1, len(arr)):
                backtrack(j, string)
        
        for i in range(len(arr)):
            backtrack(i, "")
        
        return Max