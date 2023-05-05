class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]

        heapify(piles)

        for i in range(k):
            largest = heappop(piles)
            largest //= 2
            heappush(piles, largest)
        return -sum(piles)