# Problem: Find Smallest Letter Greater Than Target
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Runtime: 0 ms
# Memory: 13.8 MB

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]