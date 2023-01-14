from collections import defaultdict

testCases = int(input())
chessBoard = []
sizes = []

for _ in range(testCases):
    size = list(map(int, input().split()))
    sizes.append(size)
    singleChessBoard = []
    for _ in range(size[0]):
        singleChessBoard.append(list(map(int, input().split())))
    chessBoard.append(singleChessBoard)

positions = []

for chess in chessBoard:
    dR = defaultdict(int)
    dL = defaultdict(int)
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            dR[i+j] += chess[i][j]
            dL[i-j] += chess[i][j]
    positions.append([dR, dL])
            
maxList = []
for index, chess in enumerate(chessBoard):
    Max = 0
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            sum = (positions[index][0][i+j] + positions[index][1][i-j]) - chess[i][j]
            Max = max(Max, sum)
    maxList.append(Max)
            
for maxL in maxList:
    print(maxL)
