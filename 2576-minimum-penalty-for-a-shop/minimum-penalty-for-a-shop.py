class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        answer = 0
        for s in customers:
            if s == "Y":
                penalty += 1
        initial = penalty
        Min = penalty
        
        # print(penalty)
        
        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty -= 1
                if penalty < Min:
                    Min = penalty
                    answer = i+1
            else:
                penalty += 1
                   

        if Min < initial:
            return answer
        return 0
