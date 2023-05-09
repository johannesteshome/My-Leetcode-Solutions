class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap) < k:
                    heappush(heap, (-nums1[i]-nums2[j], nums1[i], nums2[j]))
                elif heap[0][0] < -nums1[i]-nums2[j]:
                    heapreplace(heap, (-nums1[i]-nums2[j], nums1[i], nums2[j]))
                else: break
        
        return [[n,m] for s,n,m in heap]