class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        stack = []
        real1 = ''
        real2 = ''
        im1 = ''
        im2 = ''

        for i in range(len(num1)):
            if num1[i] == 'i':
                # print(i, 'found i', stack)
                s = ''
                while stack:
                    s += stack.pop()
                im1 = s[::-1]
            elif num1[i] == '+' and stack:
                # print(i, 'found +', stack)
                s = ''
                while stack:
                    s += stack.pop()
                real1 = s[::-1]
            else:
                stack.append(num1[i])
                # print(i, 'normal number', stack)
        
        if stack:
            s = ''
            while stack:
                s += stack.pop()
            real1 = s[::-1]

        for i in range(len(num2)):
            if num2[i] == 'i':
                s = ''
                while stack:
                    s += stack.pop()
                im2 = s[::-1]
            elif num2[i] == '+' and stack:
                s = ''
                while stack:
                    s += stack.pop()
                real2 = s[::-1]
            else:
                stack.append(num2[i])
        
        if stack:
            s = ''
            while stack:
                s += stack.pop()
            real2 = s[::-1]

        # print(real1, real2, im1, im2)
        
        ansReal = (int(real1) * int(real2)) - (int(im1) * int(im2))
        ansIm = (int(real1) * int(im2)) + (int(real2) * int(im1))
        
        return str(ansReal) + '+' + str(ansIm) + 'i'