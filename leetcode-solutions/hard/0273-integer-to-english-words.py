# Problem: Integer to English Words
# Difficulty: Hard
# URL: https://leetcode.com/problems/integer-to-english-words/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return ones[n]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")
            else:
                return ones[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 else "")
        
        result = []
        for i, unit in enumerate(thousands):
            if num == 0:
                break
            chunk = num % 1000
            if chunk:
                part = helper(chunk)
                if unit:
                    part += " " + unit
                result.append(part)
            num //= 1000
        
        return " ".join(reversed(result))