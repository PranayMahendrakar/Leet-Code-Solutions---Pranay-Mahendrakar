# Problem: Permutation Sequence
# Difficulty: Hard
# URL: https://leetcode.com/problems/permutation-sequence/
# Runtime: 0 ms
# Memory: 17.1 MB

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Calculate factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        # Available digits
        digits = list(range(1, n + 1))
        result = []
        k -= 1  # Convert to 0-indexed
        
        for i in range(n, 0, -1):
            # Which digit to pick
            idx = k // factorial[i - 1]
            result.append(str(digits[idx]))
            digits.pop(idx)
            k %= factorial[i - 1]
        
        return ''.join(result)