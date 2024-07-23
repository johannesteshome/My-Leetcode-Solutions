class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        sortedCounted = sorted(counted.items(), key=lambda x: x[1], reverse=False)
        # print(sortedCounted)
        answer = []
        # print(sortedCounted)
        sortedDic = defaultdict(list)

        for i in range(len(sortedCounted)):
            sortedDic[sortedCounted[i][1]].append(sortedCounted[i][0])

        # print(sortedDic)
        
        for key in sortedDic:
            sortedDic[key].sort(reverse= True)
            for i in range(len(sortedDic[key])):
                for _ in range(key):
                    answer.append(sortedDic[key][i])

        
        return answer