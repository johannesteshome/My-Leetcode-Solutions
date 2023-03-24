class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def cycleSort(arr):
            n = len(arr)
            i = 0
            temp = 0
            while i < n:
                correct_position = arr[i]
                if correct_position != i:
                    if correct_position >= len(arr):
                        temp = correct_position
                        i+=1
                    else:
                        arr[correct_position], arr[i] = arr[i], arr[correct_position]
                else:
                    i += 1
            print(arr)
            if temp == 0:
                return len(arr)
            return arr.index(temp)
        return cycleSort(nums)