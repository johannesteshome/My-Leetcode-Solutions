class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counted = Counter(arr)
        length = len(arr)
        percent = []

        for k in counted:
            percent.append(((counted[k]/length) * 100, k))
        
        percent = sorted(percent, reverse=True)

        return percent[0][1]

