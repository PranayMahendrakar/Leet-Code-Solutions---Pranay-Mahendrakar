# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Runtime: 28 ms
# Memory: 13.2 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length