# Count the number of prime numbers less than a
# non-negative number, n.

class Solution(object):
    lookup = {}
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(1, n):
            if self.isPrimes(i):
                count += 1
        return count

    def isPrimes(self, n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        for i in xrange(2, n/2+1):
            if n % i == 0:
                return False
        return True

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                primes[2*i: n: i] = [False] * len(primes[2*i: n: i])
        return sum(primes)


if __name__ == '__main__':
    s = Solution()
    print s.countPrimes2(99989)
