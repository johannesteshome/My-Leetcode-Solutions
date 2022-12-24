from collections import OrderedDict
# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = int(input())
items = []
nameItems = []
orderedItems = OrderedDict()

for i in range(nums):
    nameItems.append(list(input().rsplit(" ", 1)))
    if(nameItems[i][0] in orderedItems):
        orderedItems[nameItems[i][0]] += int(nameItems[i][1])
    else:
        orderedItems[nameItems[i][0]] = int(nameItems[i][1]) 


# print(nameItems)
    
for name, price in orderedItems.items():
    print(name, price)
