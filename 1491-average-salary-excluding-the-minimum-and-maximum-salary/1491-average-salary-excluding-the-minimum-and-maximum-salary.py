class Solution:
    def average(self, salary: List[int]) -> float:
        salarySum = 0

        for s in salary:
            if(s == min(salary) or s == max(salary)):
                # print(s)
                continue
            else:
                # print(s)
                salarySum = salarySum + s
                
            
                
        # print(salarySum)
        return salarySum/(len(salary)-2)