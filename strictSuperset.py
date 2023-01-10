# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(map(int, input().split()))
n = int(input())

supersetSize = len(superset)
isSuperset = True

for _ in range(n):
    newset = set(map(int, input().split()))
    
    setdiff = newset.difference(superset)
    
    
    if len(setdiff) == 0:
        if len(newset) == supersetSize:
            isSuperset = False
            break
    else:
          isSuperset = False
          break
        
print(isSuperset)
