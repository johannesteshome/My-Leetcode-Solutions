# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = n//2
        while (left <= right):
            if isBadVersion(mid):
                right = mid-1
                mid = (left+right)//2
                if not isBadVersion(right):
                    return right+1
            else:
                left = mid+1
                mid = (left+right)//2
                if isBadVersion(left):
                    return left