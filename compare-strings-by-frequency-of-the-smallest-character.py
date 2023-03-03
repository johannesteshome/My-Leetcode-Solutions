class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queriesNum = []
        wordsNum = []
        answer = []

        for query in queries:
            queriesNum.append(query.count(min(query)))

        for word in words:
            wordsNum.append(word.count(min(word)))

        wordsNum.sort()
        print(wordsNum, queriesNum)
        print(bisect_right(wordsNum, 3))
        for query in queriesNum:
            pos = int(bisect_right(wordsNum, query))
            if pos >= len(wordsNum):
                answer.append(0)
            else:
                answer.append(len(wordsNum) - pos)

        return answer