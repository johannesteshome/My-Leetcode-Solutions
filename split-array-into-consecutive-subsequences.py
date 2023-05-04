class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapArr = []

        while nums:
            found = False
            if not heapArr:
                num = heappop(nums)
                heapArr.append([num])
                continue
            
            num = heappop(nums)
            # print(heapArr)
            
            for heap in range(len(heapArr)-1, -1, -1):
                # print(heap)
                if num - heapArr[heap][-1] == 1:
                    heapArr[heap].append(num)
                    found = True
                if found:
                    break
            
            if not found:
                heapArr.append([num])
            # print(heapArr)

        for heap in range(len(heapArr)-1, -1, -1):
            if len(heapArr[heap]) < 3:
                return False
        return True