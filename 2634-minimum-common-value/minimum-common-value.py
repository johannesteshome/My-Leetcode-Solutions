class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        p1 = 0
        p2 = 0
        length1 = len(nums1)
        length2 = len(nums2)

        while p1 < length1 and p2 < length2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                return nums1[p1]
        
        return -1
        