class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        vowelsReverse = []

        newString = ""

        for i in range(len(s)):
            if s[i] in vowels:
                vowelsReverse.append(s[i])

        if len(vowelsReverse) == 0:
            return s

        vowelsI = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowels:
                newString += vowelsReverse[vowelsI]
                vowelsI += 1
            else:
                newString += s[i]
        
        return newString[::-1]