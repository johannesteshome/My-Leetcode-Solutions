class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        temp = ""
        for i in range(len(command)):
            if(command[i] == 'G'):
                answer += "G"
            elif(command[i] == "("):
                temp = ""
                temp+="("
            elif(command[i] == ")"):
                if(len(temp) == 1):
                    answer += "o"
                else:
                    answer += "al"
            else:
                temp+="a"
                
        return answer