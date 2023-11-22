class Solution:
    def countTime(self, time: str) -> int:
        hours = time[:2]
        minutes = time[3:]
        answer = 0

        if hours[0] == "?":
            if hours[1] == "?":
                answer += 24
            elif int(hours[1]) < 4:
                answer += 3
            elif int(hours[1]) >= 4:
                answer += 2
        else:
            if hours[1] == "?" and int(hours[0]) < 2:
                answer = answer + 10
            elif hours[1] == "?" and int(hours[0]) == 2:
                answer += 4
        
        if answer == 0:
            answer = 1
        
        print(answer)
        if minutes[0] == "?":
            if minutes[1] == "?":
                answer *= 60
            elif minutes[1] != "?":
                print("here", answer * 6)
                answer *= 6
        else:
            if minutes[1] == "?":
                answer *= 10
        
        return answer
        