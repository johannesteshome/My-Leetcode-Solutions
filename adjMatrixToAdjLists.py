from collections import defaultdict

nodes = int(input())
adjMatrix = []
adjLists = defaultdict(list)

for _ in range(nodes):
    row = list(map(int, input().split()))
    adjMatrix.append(row)

for i in range(nodes):
    for j in range(nodes):
        if adjMatrix[i][j] == 1:
            adjLists[i+1].append(j+1)

for val in adjLists.values():
    print(len(val), *val)