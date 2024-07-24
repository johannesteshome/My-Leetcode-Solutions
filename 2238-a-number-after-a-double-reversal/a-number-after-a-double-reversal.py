class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        snum = str(num)
        rsnum = str(int(snum[::-1]))[::-1]

        return int(rsnum) == num
