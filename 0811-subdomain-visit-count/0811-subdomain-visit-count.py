class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        arrStr = {}
        answer = []
        for cpdomain in cpdomains:
            splitted = cpdomain.split(" ")
            number  = splitted[0]
            domains = splitted[1]
            newDomains = []
            for i in range(len(domains)):
                if(domains[-i+1] == "."):
                    newDomains.append(domains[-i+2:])
                    
            newDomains.append(domains)
            for domain in newDomains:
                if(domain not in arrStr):
                    arrStr[domain] = int(number)
                else:
                    arrStr[domain] += int(number)
            
        # print(arrStr)
        
        for key in arrStr:
            answer.append(str(arrStr[key]) + " " + key)
            
        return answer