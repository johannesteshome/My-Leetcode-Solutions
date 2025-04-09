class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # the general steps 
        # 1. I will heapify the list
        # 2. heappop the smallest element 
        # 3. subtract it from the entire array
        # 4. repeat from step 1
        
        steps = 0

        heapify(nums)

        while nums:
            smallest_el = heappop(nums)

            if smallest_el == 0:
                continue

            for i in range(len(nums)):
                nums[i] -= smallest_el

            heapify(nums)
            steps += 1

        return steps
