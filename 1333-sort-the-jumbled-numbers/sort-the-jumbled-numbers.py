class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        sortedDic = defaultdict(list)
        numList = []
        ans = []

        for index, num in enumerate(nums):
            mapped = ""
            tnum = str(num)

            for i in range(len(tnum)):
                mapped += str(mapping[int(tnum[i])])
            
            numList.append((int(mapped), index))
        
        numList.sort()
        # print(numList)

        for num in numList:
            ans.append(nums[num[1]])

        return ans