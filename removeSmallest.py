testCases = int(input())

for _ in range(testCases):
    found = False
    size = int(input())
    list1 = list(map(int, input().split()))
    
    if size == 1:
        print("YES")
        continue

    difference = []
    list1.sort()

    for i in range(size-1, 0, -1):
        difference.append(list1[i] - list1[i-1])
    
    for d in difference:
        if d > 1:
            print("NO")
            found = True
            break
    if found: 
        continue
    print("YES")
