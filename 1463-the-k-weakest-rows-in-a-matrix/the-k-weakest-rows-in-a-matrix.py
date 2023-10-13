class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            heap.append((mat[i].count(1), i))
        
        heapify(heap)
        # print(heap)
        answer = []

        for _ in range(k):
            answer.append(heappop(heap)[1])
        
        return answer
        