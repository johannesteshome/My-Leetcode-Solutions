class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightIndex = []
        for i in range(len(names)):
                heightIndex.append((heights[i], i))
        
        heightIndex.sort(reverse = True)

        answer = []

        for i in range(len(names)):
            answer.append(names[heightIndex[i][1]])
        
        return answer