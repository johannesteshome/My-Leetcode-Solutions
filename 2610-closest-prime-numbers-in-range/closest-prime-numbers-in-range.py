class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        p = 2
        while (p * p <= right):

            if (prime[p] == True):

                for i in range(p * p, right+1, p):
                    prime[i] = False
            p += 1
        
        Min = float("inf")
        primes = []

        for i in range(left, right + 1):
            if prime[i] and i != 1:
                primes.append(i)
        # print(primes)
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if Min > diff:
                Min = diff
                num1 = primes[i]
                num2 = primes[i+1]
        
        if Min == float("inf"):
            return [-1,-1]
        
        return [num1, num2]

