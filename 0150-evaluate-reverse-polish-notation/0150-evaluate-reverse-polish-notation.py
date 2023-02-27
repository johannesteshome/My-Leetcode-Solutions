class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                sign = token
                operand2 = stack.pop()
                operand1 = stack.pop()
                if sign == "+":
                    stack.append(operand1 + operand2)
                elif sign == "-":
                    stack.append(operand1 - operand2)
                elif sign == "*":
                    stack.append(operand1 * operand2)
                elif sign == "/":
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
                
        return stack.pop()
        
        