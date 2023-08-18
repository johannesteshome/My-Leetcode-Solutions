class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counterArray = []
        for word in words:
            counterArray.append(Counter(word))

        common_keys = set(counterArray[0].keys())

        for dictionary in counterArray[1:]:
            common_keys = common_keys.intersection(dictionary.keys())
        
        ans = defaultdict(lambda: float('inf'))
        
        for dictionary in counterArray:
            for key in common_keys:
                ans[key] = min(dictionary[key], ans[key])

        answer = []

        for a in ans:
            for _ in range(ans[a]):
                answer.append(a)
        
        return answer
