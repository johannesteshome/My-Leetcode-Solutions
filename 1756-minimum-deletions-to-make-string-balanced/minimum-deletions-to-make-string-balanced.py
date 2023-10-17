class Solution:
    def minimumDeletions(self, s: str) -> int:
        deleteA = [0] * (len(s) + 1)
        deleteB = [0] * (len(s) + 1)

        for i in range(len(s)):
            if s[i] == "b":
                deleteB[i+1] = deleteB[i] + 1
            else:
                deleteB[i+1] = deleteB[i]
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == "a":
                deleteA[len(s)-1-i+1] = deleteA[len(s)-1-i] + 1
            else:
                deleteA[len(s)-1-i+1] = deleteA[len(s)-1-i]
        
        deleteA = deleteA[::-1]

        Min = float("inf")
        for i in range(len(deleteA)):
            Min = min(Min, deleteA[i] + deleteB[i])
        
        return Min

        