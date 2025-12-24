# Problem: Minimum Window Substring
# Difficulty: Hard
# URL: https://leetcode.com/problems/minimum-window-substring/
# Runtime: 128 ms
# Memory: 12.8 MB

class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        from collections import Counter
        t_count = Counter(t)
        required = len(t_count)
        
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        ans = float('inf'), None, None
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]