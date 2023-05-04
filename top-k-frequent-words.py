class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countWords = Counter(words)
        print(countWords.items())
        heap = []
        answer = []

        for keys, value in countWords.items():
            countWords[keys] *= -1
        
        for keys, value in countWords.items():
            heappush(heap, (value, keys))
        
        for _ in range(k):
            answer.append(heappop(heap)[1])
        
        return answer