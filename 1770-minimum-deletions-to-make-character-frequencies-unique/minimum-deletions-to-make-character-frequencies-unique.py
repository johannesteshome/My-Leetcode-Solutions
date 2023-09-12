class Solution:
    def minDeletions(self, s: str) -> int:
        strCount = Counter(s)
        counts = set()
        count = list(strCount.values())
        count.sort(reverse=True)
        # print(count)
        answer = 0

        for i in count:
            # print(i)
            while i in counts:
                i -= 1
                answer += 1
            if i != 0:
                counts.add(i)
        
        return answer
        