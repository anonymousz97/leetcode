class Solution:
    def __init__(self):
        self.lst_prime = self.sieve_of_eratosthenes(10**6)
        self.lst_dist = [self.lst_prime[x+1]-self.lst_prime[x] for x in range(len(self.lst_prime[:-1]))]
        
    def sieve_of_eratosthenes(self, n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return [i for i in range(n + 1) if primes[i]]
                
    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_v = 99999999
        idx_min = -1
        for idx, i in enumerate(self.lst_prime[:-1]):
            if i >= left and self.lst_prime[idx+1] <= right:
                if self.lst_dist[idx] < min_v:
                    min_v = self.lst_dist[idx]
                    idx_min = idx
        if min_v == 99999999:
            return [-1, -1]
        return [self.lst_prime[idx_min], self.lst_prime[idx_min+1]]

            

        