# Problem: Reverse Vowels of a String
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Runtime: 15 ms
# Memory: 13.8 MB

class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)