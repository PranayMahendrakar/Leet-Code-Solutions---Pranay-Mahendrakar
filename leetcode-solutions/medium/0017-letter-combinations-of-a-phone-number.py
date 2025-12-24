# Problem: Letter Combinations of a Phone Number
# Difficulty: Medium
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return
            
            for letter in phone[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result