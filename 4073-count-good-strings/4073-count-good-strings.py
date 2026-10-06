class Solution(object):
    def countGoodStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def fib(m):  # (F(m), F(m + 1)) by fast doubling
            if m == 0:
                return (0, 1)
            a, b = fib(m >> 1)
            c = a * (2 * b - a) % MOD
            d = (a * a + b * b) % MOD
            if m & 1:
                return (d, (c + d) % MOD)
            return (c, d)

        return 2 * fib(n)[0] % MOD