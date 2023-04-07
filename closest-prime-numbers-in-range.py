class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime
        primesBetween = []
        primes = prime_sieve(right)
        for i in range(left, right+1):
            if primes[i]:
                primesBetween.append(i)
        Min = float("inf")
        answer = []

        if len(primesBetween) <= 1:
            return [-1, -1]

        for i in range(len(primesBetween) - 1):
            if primesBetween[i+1] - primesBetween[i] < Min:
                Min = primesBetween[i+1] - primesBetween[i]
                answer = []
                answer.append(primesBetween[i])
                answer.append(primesBetween[i+1])
        
        return answer