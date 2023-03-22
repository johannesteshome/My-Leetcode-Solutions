class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        answer = ""
        final = 0
        def findK(num):
            nonlocal final
            nonlocal answer
            if n == final:
                return 
            
            invertNum = ''.join(['1' if i == '0' else '0' for i in num])
            num += '1' + invertNum[::-1]
            answer = num
            final += 1
            findK(num)
        
        findK("0")
        return answer[k-1]