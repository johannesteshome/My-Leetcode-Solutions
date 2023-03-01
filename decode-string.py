class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        stack = []
        if len(s) == 1:
            if s[0].isnumeric():
                return ""
            else:
                return s        
        def decode(i):
            if i == len(s):
                return
            elif s[i].isnumeric():
                stack.append(s[i])
                return decode(i+1)
            elif s[i] == '[':
                stack.append('[')
                return decode(i+1)
            elif s[i] == ']':
                string = ""
                num = ""
                while stack[-1] != '[':
                    if len(stack) == 0:
                        break
                    string += stack.pop()
                stack.pop()
                while stack[-1] != '[':
                    if stack[-1].isnumeric():
                        num += stack.pop()
                    else:
                        break
                    if len(stack) == 0:
                        break
                # stack.pop()
                print(stack)
                print(num)
                print(string)
                num = num[::-1]
                num = int(num)
                string = string[::-1]
                string = num * string
                stack.append(string[::-1])
                return decode(i+1)
            else:
                stack.append(s[i])
                return decode(i+1)

        decode(i)
        answer = ""
        for s in stack:
            answer += s[::-1]
        return answer