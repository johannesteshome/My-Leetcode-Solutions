class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        left = 1
        right = x
        mid = x//2
        while (left <= right):
            if mid*mid > x:
                right = mid-1
                mid = (left+right)//2
                if right*right <= x:
                    return right
            elif mid*mid < x:
                left = mid+1
                mid = (left+right)//2
                if left*left >= x:
                    return left-1
            elif mid*mid == x:
                return mid