testCases = int(input())
nums = []

for _ in range(testCases):
    size = int(input())
    nums = list(map(int, input().split()))
    Max = 0
    Sum = 0
    for num in nums:
        if num > 0:
            if Max < 0:
                Sum += Max
            Max = max(Max, num)
        elif num < 0:
            if Max > 0:
                Sum += Max
                Max = num
            elif Max == 0:
                Max = num
            Max = max(Max, num)
    Sum += Max
    print(Sum)
