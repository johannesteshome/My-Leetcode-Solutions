class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split(" ")

        if len(words) == 1:
            if words[0][-1] != words[0][0]:
                return False
            return True


        for i in range(len(words) - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        
        if words[-1][-1] != words[0][0]:
            return False
        
        return True

        