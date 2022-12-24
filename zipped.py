# Enter your code here. Read input from STDIN. Print output to STDOUT
# taking input of the student and subject sizes
subStudNums = list(map(int, input().split()))
subMarks = []

# taking input of the marks of the subject
for i in range(subStudNums[1]):
    subMarks.append(list(map(float, input().split())))
    
X = []

#putting the subject mark in an array 
for i in range(len(subMarks)):
    X.append(subMarks[i])

# zipping the marks and calculating the average
for i in zip(*X):
    print(sum(i)/subStudNums[1])
    
