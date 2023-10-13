class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for c in count:
            heap.append((-count[c], c))
        
        answer = []
        # print(heap)
        heapify(heap)

        for _ in range(k):
            # print(heappop(heap))
            # # print(heap)
            answer.append(heappop(heap)[1])
        
        return answer
