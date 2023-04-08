nodes = int(input())
adjMatrix = []
Max = 0

for _ in range(nodes):
    row = list(map(int, input().split()))
    adjMatrix.append(row)

roadCount = 0

for row in adjMatrix:
    roadCount += row.count(1)

print(roadCount//2)