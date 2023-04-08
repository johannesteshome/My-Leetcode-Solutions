from collections import defaultdict

nodes = int(input())

# adjMatrix = [[0] * nodes] * nodes
adjLists = defaultdict(list)

operations = int(input())

for _ in range(operations):
    op = list(map(int, input().split()))
    if op[0] == 1:
        adjLists[op[1]].append(op[2])
        adjLists[op[2]].append(op[1])
    else:
        print(*adjLists[op[1]])