class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        # print(arr)
        answer = ""

        for a in arr:
            answer += a[::-1]
            answer += " "
        
        return answer[:-1]
        