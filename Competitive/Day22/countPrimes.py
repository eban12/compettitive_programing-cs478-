class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [1] * n
        primes[0] = primes[1] = 0

        current = 2
        while current * current < n:
            if primes[current] == 1:
                for i in range(2 * current,n,current):
                    primes[i] = 0

            if current == 2:
                current += 1
            else:
                current += 2
        return sum(primes)
