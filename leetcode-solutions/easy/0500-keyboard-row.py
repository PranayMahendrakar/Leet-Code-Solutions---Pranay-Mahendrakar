# Problem: Keyboard Row
# Difficulty: Easy
# URL: https://leetcode.com/problems/keyboard-row/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def findWords(self, words):
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        return [w for w in words if any(set(w.lower()) <= row for row in rows)]