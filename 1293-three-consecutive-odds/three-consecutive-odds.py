class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left = 0
        right = 0

        while right < len(arr):
            if arr[right] % 2 != 0:
                if right - left + 1 == 3:
                    print(left, right)
                    return True
                right += 1
            else:
                right += 1
                left = right
        
        return False
            

