class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        k1 = w1.keys()
        k2 = w2.keys()
        # print(k1, k2)

        w1 = sorted(list(w1.values()))
        w2 = sorted(list(w2.values()))
        # print(w1, w2)

        return w1 == w2 and k1 == k2