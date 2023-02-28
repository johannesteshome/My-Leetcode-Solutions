class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def reverse(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            return reverse(left+1, right-1)
            
        left = 0
        right = len(s) - 1
        reverse(left, right)