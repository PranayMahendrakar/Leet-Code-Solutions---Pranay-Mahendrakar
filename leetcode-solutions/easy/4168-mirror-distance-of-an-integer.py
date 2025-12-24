# Problem: Mirror Distance of an Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
        def mirrorDistance(self, n):
                    """
                            :type n: int
                                    :rtype: int
                                            """""
                    # Reverse the integer
                    rev = int(str(n)[::-1])
                    return abs(n - rev)