nodes = int(input())
adjMatrix = []

for i in range(nodes):
    adjMatrix.append(list(map(int, input().split())))

otherWay = list(zip(*adjMatrix))
sources = []
sinks = []

for i in range(nodes):
    if all(element == 0 for element in adjMatrix[i]):
        sinks.append(i+1)
    if all(element == 0 for element in otherWay[i]):
        sources.append(i+1)

print(len(sources), *sources)
print(len(sinks), *sinks)