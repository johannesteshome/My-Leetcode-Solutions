class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        answer = []

        
        

        def dfs(curr, limit):

            if curr > limit:
                return 
            
            answer.append(curr)
            
            for i in range(0, 10):
                nextNum = (curr * 10) + i
                dfs(nextNum, limit)
        
        for i in range(1, 10):
            dfs(i, n)

        return answer