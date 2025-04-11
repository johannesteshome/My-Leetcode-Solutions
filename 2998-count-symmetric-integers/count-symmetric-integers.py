class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0
        
        for num in range(low, high + 1):
            strNum = str(num)

            if len(strNum) % 2 == 0:
                half = len(strNum) // 2
                firstHalf = strNum[:half]
                secondHalf = strNum[half:]

                sum1 = 0
                sum2 = 0

                for i in range(len(firstHalf)):
                    sum1 += int(firstHalf[i])
                for i in range(len(secondHalf)):
                    sum2 += int(secondHalf[i])

                if sum1 == sum2:
                    count += 1
                
                # print(firstHalf, secondHalf)
        
        return count