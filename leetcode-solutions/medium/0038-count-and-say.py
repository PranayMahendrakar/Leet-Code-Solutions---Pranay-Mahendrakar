# Problem: Count and Say
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-and-say/
# Runtime: 11 ms
# Memory: 12.4 MB

class Solution(object):
    def countAndSay(self, n):
        result = "1"
        
        for _ in range(n - 1):
            new_result = ""
            i = 0
            while i < len(result):
                char = result[i]
                count = 1
                while i + count < len(result) and result[i + count] == char:
                    count += 1
                new_result += str(count) + char
                i += count
            result = new_result
        
        return result