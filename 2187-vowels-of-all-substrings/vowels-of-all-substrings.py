class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        answer = 0

        for i in range(len(word)):
            if word[i] in vowels:
                n = len(word) - i
                answer += (n * (i + 1))
        
        return answer