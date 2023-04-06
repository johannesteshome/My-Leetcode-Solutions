class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xSet = False

        for i in range(32):
            if x & (1 << i) != 0:
                xSet = True
            else: xSet = False

            if y & (1 << i) != 0:
                if not xSet:
                    count += 1
            else:
                if xSet:
                    count += 1

        return count