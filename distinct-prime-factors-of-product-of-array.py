class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def sieve(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
            return [i for i in range(n + 1) if primes[i]]

        
        max_num = max(nums)
        primes = sieve(int(max_num ** 0.5) + 1)
        factors = set()
        for num in nums:
            for p in primes:
                while num % p == 0:
                    factors.add(p)
                    num //= p
                if p > num:
                    break
            if num > 1:
                factors.add(num)
        return len(factors)