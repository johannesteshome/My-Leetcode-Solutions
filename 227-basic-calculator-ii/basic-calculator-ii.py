class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            # print(s[i])
            if s[i] == " ":
                i+=1
                continue
            
            if s[i].isdigit():
                num = ""
                while i<len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                num = int(num)
                if stack and (stack[-1] == '*' or stack[-1] == "/"):
                    operator = stack.pop()
                    num2 = stack.pop()
                    # print(operator, num2)
                    if operator == "*":
                        stack.append(num*num2)
                    else:
                        stack.append(num2//num)
                else:
                    stack.append(num)
            else:
                # print("here")
                stack.append(s[i])
                i += 1
            
        
        # print(stack)
        stack = stack[::-1]
        if stack:
            while len(stack) != 1:
                # print(stack)
                num2 = stack.pop()
                operator = stack.pop()
                num1 = stack.pop()

                if operator == '+':
                    stack.append(num1 + num2)
                else:
                    stack.append(num2 - num1)
        
        return stack[0]

            
        