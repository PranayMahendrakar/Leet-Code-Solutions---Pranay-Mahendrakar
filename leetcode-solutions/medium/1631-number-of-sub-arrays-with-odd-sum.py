# Problem: Number of Sub-arrays With Odd Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Runtime: 74 ms
# Memory: 22.1 MB

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        # Track count of even and odd prefix sums
        even_count = 1  # Empty prefix has sum 0 (even)
        odd_count = 0
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                # Current prefix is even, need odd prefix before
                result += odd_count
                even_count += 1
            else:
                # Current prefix is odd, need even prefix before
                result += even_count
                odd_count += 1
            
            result %= MOD
        
        return result