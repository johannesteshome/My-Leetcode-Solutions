class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        ans = 0
        # print(count)
        for word in words:
            found = True
            c = Counter(word)
            for k in c:
                if k in count and count[k] >= c[k]:
                    continue
                found = False
            if found:
                ans += len(word)
        return ans
        