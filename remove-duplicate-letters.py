class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        Map = defaultdict(int)
        stack = []
        answer = ""

        for i in range(len(s)):
            Map[s[i]] = i
        # print(Map)
        for index, char in enumerate(s):
            print(stack)
            if not stack:
                stack.append(char)
            if stack and stack[-1] < char and char not in stack:
                stack.append(char)
            elif stack and stack[-1] > char and char not in stack:
                print("here")
                while stack and stack[-1] > char and Map[stack[-1]] > index:
                    stack.pop()
                stack.append(char)

        print(stack)
        return ''.join(map(str, stack))