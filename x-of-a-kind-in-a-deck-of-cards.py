class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        factors = []

        # def gcd(a, b):
        #     if b == 0:
        #         return a
        #     return gcd(b, a % b)

        def primes(n):
            factorization = []
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
            
            return factorization

        def is_prime(num):
 
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return True
            return False

        counted = Counter(deck)

        for val in counted.values():
            factors.append(primes(val))

        if len(deck) == len(counted.values()):
            return False
        freq = list(counted.values())

        if len(freq) == 1:
            if freq[0] == 1:
                return False
            if freq[0] == 2:
                return True
            return is_prime(freq[0])

        intersection = set(factors[0])
        for i in range(1, len(factors)):
            intersection = intersection & set(factors[i])

        if len(intersection) == 0:
            return False
        return True
        # GCD = gcd(freq[0], freq[1])

        # if GCD == 1:
        #     return False

        # for i in range(len(freq) - 1):
        #     if gcd(freq[i], freq[i+1]) != GCD:
        #         return False
        
        # return True