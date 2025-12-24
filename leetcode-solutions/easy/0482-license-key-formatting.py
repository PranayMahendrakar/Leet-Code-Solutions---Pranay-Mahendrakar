# Problem: License Key Formatting
# Difficulty: Easy
# URL: https://leetcode.com/problems/license-key-formatting/
# Runtime: 2 ms
# Memory: 14 MB

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        remainder = len(s) % k
        groups = [s[:remainder]] if remainder else []
        groups.extend(s[i:i+k] for i in range(remainder, len(s), k))
        return '-'.join(groups)