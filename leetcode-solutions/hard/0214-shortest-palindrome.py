# Problem: Shortest Palindrome
# Difficulty: Hard
# URL: https://leetcode.com/problems/shortest-palindrome/
# Runtime: 82 ms
# Memory: 19.2 MB

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        # Use KMP failure function to find longest palindrome prefix
        # Create pattern: s + '#' + reverse(s)
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        
        # KMP failure function
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        # lps[-1] gives length of longest palindrome prefix
        longest_palindrome_prefix = lps[-1]
        
        # Add remaining characters in reverse to front
        to_add = rev[:len(s) - longest_palindrome_prefix]
        return to_add + s