n = list(map(int, input().split()))
words = []
 
for i in range(n[0]):
    word = input()
    words.append(word)
colWords = list(zip(*words))
 
word = []
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in words[i][:j]+words[i][j+1:] or words[i][j] in colWords[j][:i]+colWords[j][i+1:]:
            continue
        else: 
            word.append(words[i][j])
 
word = ''.join(map(str, word))
print(word)
