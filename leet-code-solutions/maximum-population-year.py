class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        if len(logs) == 1:
            return logs[0][0]

        logs.sort()
        deaths = []
        pop = 0
        Max = float("-inf")


        for birth, death in logs:
            pop += 1

            dead = bisect_right(deaths, birth)
            if pop-dead > Max:
                year = birth
                Max = pop-dead

            deaths.append(death)
            deaths.sort()
        
        
        return year