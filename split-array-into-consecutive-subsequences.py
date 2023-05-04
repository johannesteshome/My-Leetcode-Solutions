class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # create an array to store all possible subsequences of the array
        heapArr = []

        # iterate through the list with min-heap
        while nums:
            found = False

            # pop the minimum item in the list           
            num = heappop(nums)
            
            # from the list of subsequences start from the last subsequence to add the item because the last subsequence probably not have satisfied the rule of having length of 3 or more
            for heap in range(len(heapArr)-1, -1, -1):
                if num - heapArr[heap][-1] == 1:
                    heapArr[heap].append(num)
                    found = True
                if found:
                    break
            
            if not found:
                heapArr.append([num])

        # from the lists check if all have length of 3 or more
        for heap in range(len(heapArr)-1, -1, -1):
            if len(heapArr[heap]) < 3:
                return False
        return True