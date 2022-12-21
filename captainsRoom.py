# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
roomNums = [int(i) for i in input().split(' ')]

group = len(roomNums) // size

roomList = {}

for i in roomNums:
    if(roomList.get(i) != None):
        count = roomList.get(i)
        count = count+1
        roomList.update({i: count})
    else:
        roomList.update({i: 1})
        
for room in roomList:
    if(roomList.get(room) == 1):
        print(room)
    
