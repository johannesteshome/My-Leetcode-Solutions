class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        sortedDic = defaultdict(list)
        ans = []

        for num in nums:
            mapped = ""
            tnum = num
            while tnum != 0:
                temp = tnum%10
                mapped += str(mapping[temp])
                tnum //= 10
            if num == 0:
                mapped += str(mapping[num])
            
            if mapped == "":
                mapped = 0
            else:
                mapped = int(mapped[::-1])
            sortedDic[mapped].append(num)
        
        print(sortedDic)
        sortedDic = sorted(sortedDic.items())

        for key in sortedDic:
            # print(key)
            for i in range(len(key[1])):
                # print(sortedDic[key][i])
                ans.append(key[1][i])

        return ans