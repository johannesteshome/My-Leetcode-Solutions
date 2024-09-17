class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = defaultdict(int)
        answer = []

        words1 = s1.split()
        words2 = s2.split()

        for word in words1:
            count[word] += 1
        
        for word in words2:
            count[word] += 1

        for key in count:
            if count[key] == 1:
                answer.append(key)
        
        return answer