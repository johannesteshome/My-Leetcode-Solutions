class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        left = 0
        right = length - 1

        while left <= right:
            mid = (left+right)//2
            if citations[mid] == length - mid:
                return length - mid
            elif citations[mid] < length - mid:
                left = mid + 1
            elif citations[mid] > length - mid:
                right = mid - 1

        return length - left