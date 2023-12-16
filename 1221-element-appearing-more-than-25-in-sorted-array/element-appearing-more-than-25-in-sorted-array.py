class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counted = Counter(arr)
        length = len(arr)

        for k in counted:
            if counted[k] > length / 4:
                return k
    