# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        primes = [True]*(n)
        primes[0] = False
        primes[1] = False
        i = 2
        while i*i < n:
            if primes[i] == True:
                for j in range(2*i,n,i):
                    primes[j] = False
            i += 1
        return primes.count(True)