from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        firstNum = ""
        num = ""
        temp = ""
        op = ""
        lastNum = 0
        
        for i in range(len(expression)):
            # print(expression[i])
            # print(lastNum)
            # print(expression[i] == '/')
            if expression[i] == '/':
                num = temp
                temp = ""
            elif (expression[i] == "+" or expression[i] == "-") and i != 0:
                if op != "":
                    if op == "+":
                        lastNum += (float(num) / float(temp))
                        op = expression[i]
                    else:
                        lastNum -= (float(num) / float(temp))
                        op = expression[i]
                else:
                    op = expression[i]
                    lastNum = float(num) / float(temp)
                temp = ""
                num = ""
            else:
                temp += expression[i]
        
        if op != "":
            if op == "+":
                lastNum += (float(num) / float(temp))
            else:
                lastNum -= (float(num) / float(temp))
        else:
            return expression

        fraction = str(Fraction(lastNum).limit_denominator())

        if '/' not in fraction:
            return fraction + '/1'
        
        return fraction