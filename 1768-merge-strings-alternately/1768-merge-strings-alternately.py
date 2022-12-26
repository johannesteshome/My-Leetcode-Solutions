class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        for i in range(min(len(word1), len(word2)) + 1):
            if(i <= min(len(word1), len(word2)) - 1):
                mergedStr += word1[i]
                print(i)
                mergedStr += word2[i]
            else:
                mergedStr +=word1[i:]
                mergedStr += word2[i:]
                
        return mergedStr