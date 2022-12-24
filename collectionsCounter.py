# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoesNum = int(input())
shoesSizes = list(map(int, input().split()))

custNum = int(input())
custDemand = []

for i in range(custNum):
    custDemand.append(list(map(int, input().split())))
    

prices = 0

shoes = Counter(shoesSizes)
    
for i in range(len(custDemand)):
    if(custDemand[i][0] in shoes and shoes[custDemand[i][0]] > 0):
        prices += custDemand[i][1]
        shoes[custDemand[i][0]] = shoes[custDemand[i][0]] - 1

      
print(prices)

