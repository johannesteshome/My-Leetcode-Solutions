# Enter your code here. Read input from STDIN. Print output to STDOUT
numInput = int(input())
stringArray = []
wordCount = {}
for x in range(numInput):
    word = input()
    stringArray.append(word)
    
    
    
for i in range(len(stringArray)):
    if(wordCount.get(stringArray[i]) != None):
        count = wordCount.get(stringArray[i]) + 1
        wordCount.update({stringArray[i]: count})
    else:
        wordCount[stringArray[i]] = 1
    

                
print(len(wordCount))
for word in wordCount:
    print(wordCount[word], end = ' ')
