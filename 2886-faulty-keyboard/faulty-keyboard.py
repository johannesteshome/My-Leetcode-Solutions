class Solution:
    def finalString(self, s: str) -> str:
        answer = ""

        for i in range(len(s)):
            if s[i] != 'i':
                answer += s[i]
            else:
                answer = answer[::-1]
        
        return answer