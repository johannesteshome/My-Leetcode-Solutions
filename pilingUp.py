# Enter your code here. Read input from STDIN. Print output to STDOUT
testcases = int(input())

for i in range(testcases):
    blockSize = int(input())
    blocks = [int(i) for i in input().split(' ')]
    
    top = blocks[0] if blocks[0]>blocks[-1] else blocks[-1]
    left, right = 0, blockSize-1
    
    while(left < right):
        if(blocks[left] >= blocks[right]):
            if(top >= blocks[left]):
                top = blocks[left]
                left+=1
            else:
                print("No")
                break
        
        else:
            if(top >= blocks[right]):
                top = blocks[right]
                right-=1
            else:
                print("No")
                break
    if(left == right): 
        print("Yes")
        
