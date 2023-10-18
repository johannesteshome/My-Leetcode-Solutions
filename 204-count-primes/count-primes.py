class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n+1)
            is_prime[0] = is_prime[1] = False
            p = 2

            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n+1, p):
                        is_prime[i] = False
                p += 1

            primes = [i for i in range(n+1) if is_prime[i]]
            
            return primes

        
        primes = sieve_of_eratosthenes(n-1)
        print(primes)

        return len(primes)