class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        answer = []
        checks = {
            "hR": [],
            "hL": [],
            "vU": [],
            "vD": [],
            "dDU": [],
            "dDD": [],
            "dUU": [],
            "dUD": []
        }
        
        for queen in queens:
            changeX = queen[0] - king[0]
            changeY = queen[1] - king[1]
            distance = sqrt(changeX**2 +changeY**2)
            
            if(changeX == 0):
                if(queen[1] > king[1]):
                    checks["hR"].append([queen, distance])
                else:
                    checks["hL"].append([queen, distance])
            elif(changeY == 0):
                if(queen[0] < king[0]):
                    checks["vU"].append([queen, distance])
                else:
                    checks["vD"].append([queen, distance])
            elif(changeY/changeX == 1):
                if(queen[0] < king[0]):
                    checks["dDU"].append([queen, distance])
                else:
                    checks["dDD"].append([queen, distance])
            elif(changeY/changeX == -1):
                if(queen[0] < king[0]):
                    checks["dUU"].append([queen, distance])
                else: 
                    checks["dUD"].append([queen, distance])
                    
        # print(checks)
        
        for check in checks.values():
            if(len(check) != 0):
                check.sort(key = lambda x: x[1])
                answer.append(check[0][0])
        return answer