class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for index in range(len(words)-1):
            for wordIndex in range(min(len(words[index]), len(words[index+1]))):
                if(words[index][wordIndex] == words[index+1][wordIndex]):
                    if(wordIndex == min(len(words[index]), len(words[index+1])) - 1):
                        if(len(words[index+1]) < len(words[index])): return False
                    else:
                        continue
                elif(order.index(words[index][wordIndex]) < order.index(words[index+1][wordIndex])):
                    break
                else:
                    return False
                
        
        return True