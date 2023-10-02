class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            # print("here")
            if not stack:
                stack.append([s[i], 1])
            elif stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
            if stack[-1][1] == k:
                stack.pop()
        
        # print(stack)
        answer = ""
        for i in range(len(stack)):
            for j in range(stack[i][1]):
                answer += stack[i][0]
        
        return answer