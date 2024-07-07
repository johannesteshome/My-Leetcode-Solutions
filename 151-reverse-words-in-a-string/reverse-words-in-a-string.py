class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        answer = ""

        for i in range(len(splitted) - 1, -1, -1):
            answer += splitted[i]
            if i != 0:
                answer += " "
        
        return answer