class Solution:
    def freqAlphabets(self, s: str) -> str:
        digitMaps = {}
        for i in range(26):
            digitMaps[i+1] = chr(ord('a') + i)
                
        digitStack = ""
        word = ""
        
        print(digitMaps)
        
        # strArr = s.split(" ")
        # print(strArr)
        
        
        while(s != ""):
            if(s[-1].isnumeric()):
                word += digitMaps[int(s[-1])]
                s = s[:-1]
            else:
                s = s[:-1]
                letter = s[-2:]
                word += digitMaps[int(letter)]
                s = s[:-2]
                
        return word[::-1]


            