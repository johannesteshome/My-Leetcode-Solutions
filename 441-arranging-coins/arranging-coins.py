class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            # print(mid)

            res = (mid*(mid+1)) // 2

            if res < n:
                left = mid + 1
            elif res > n:
                right = mid - 1
            else:
                return mid
        
        return right
        