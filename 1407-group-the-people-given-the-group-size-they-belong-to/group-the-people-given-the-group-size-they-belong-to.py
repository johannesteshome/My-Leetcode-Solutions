class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = defaultdict(list)
        answer = []

        for i in range(len(groupSizes)):
            hashmap[groupSizes[i]].append(i)
            if groupSizes[i] == len(hashmap[groupSizes[i]]):
                answer.append(hashmap[groupSizes[i]])
                hashmap[groupSizes[i]] = []
        
        for key in hashmap:
            if len(hashmap[key]) >= 1:
                answer.append(hashmap[key])
        
        return answer
        