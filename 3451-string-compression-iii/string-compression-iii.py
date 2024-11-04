class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''

        i = 0
        length = 1

        while i < (len(word) - 1):
            if word[i] != word[i+1] or (word[i] == word[i+1] and length == 9):
                comp += str(length)
                comp += word[i]
                length = 1
            elif word[i] == word[i+1]:
                length += 1
                
            i += 1
        
        comp += str(length)
        comp += word[i]

        return comp