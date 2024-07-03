class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        numsList = defaultdict(list)

        answer = [[], []]

        for i in range(len(nums1)):
            numsList[nums1[i]].append(0)

        for i in range(len(nums2)):
            numsList[nums2[i]].append(1)
        
        print(numsList)
        
        for k in numsList:
            if len(set(numsList[k])) == 1:
                answer[numsList[k][0]].append(k)
        
        return answer