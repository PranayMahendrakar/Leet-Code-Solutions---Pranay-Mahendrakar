# Problem: Expression Add Operators
# Difficulty: Hard
# URL: https://leetcode.com/problems/expression-add-operators/
# Runtime: 624 ms
# Memory: 13 MB

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        n = len(num)
        
        def backtrack(index, path, value, prev):
            if index == n:
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, n):
                # Skip numbers with leading zeros (except "0" itself)
                if i > index and num[index] == '0':
                    break
                
                curr_str = num[index:i+1]
                curr = int(curr_str)
                
                if index == 0:
                    # First number, no operator
                    backtrack(i + 1, curr_str, curr, curr)
                else:
                    # Addition
                    backtrack(i + 1, path + '+' + curr_str, value + curr, curr)
                    # Subtraction
                    backtrack(i + 1, path + '-' + curr_str, value - curr, -curr)
                    # Multiplication - need to adjust for precedence
                    backtrack(i + 1, path + '*' + curr_str, value - prev + prev * curr, prev * curr)
        
        backtrack(0, "", 0, 0)
        return result