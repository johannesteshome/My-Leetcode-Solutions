class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        index1 = 1
        digit1 = 1
        num1Int = 0
        while(index1 <= len(num1)):
            num1Int = num1Int + (int(num1[-index1]) * digit1)
            digit1 = digit1 * 10
            index1 = index1 + 1
        
        index2 = 1
        digit2 = 1
        num2Int = 0
        while(index2 <= len(num2)):
            num2Int = num2Int + (int(num2[-index2]) * digit2)
            digit2 = digit2 * 10
            index2 = index2 + 1
            
        return str(num1Int * num2Int)
        