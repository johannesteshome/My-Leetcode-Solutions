class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                return 1
            return 2
        
        checker = []
        left = 0
        right = 1
        Max = float("-inf")
        
        while right < len(arr):
            # print(checker)
            if arr[left] == arr[right]:
                # print("is equal")
                left += 1
                right += 1
                if len(checker) > 0:
                    Max = max(Max, len(checker))
                    checker = []
            elif arr[left] > arr[right]:
                # print("is greater")
                if len(checker) == 0:
                    checker.append(1)
                    left += 1
                    right += 1
                elif checker[-1] == 0:
                    checker.append(1)
                    left += 1
                    right += 1
                else:
                    Max = max(Max, len(checker))
                    checker = []
                    checker.append(1)
                    left += 1
                    right += 1
            elif arr[left] < arr[right]:
                # print("is less")
                if len(checker) == 0:
                    checker.append(0)
                    left += 1
                    right += 1
                elif checker[-1] == 1:
                    checker.append(0)
                    left += 1
                    right += 1
                else:
                    Max = max(Max, len(checker))
                    checker = []
                    checker.append(0)
                    left += 1
                    right += 1
                    
        Max = max(Max, len(checker))
        
        return Max + 1
        