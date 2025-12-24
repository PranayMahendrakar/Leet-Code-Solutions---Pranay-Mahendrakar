# Problem: Fraction to Recurring Decimal
# Difficulty: Medium
# URL: https://leetcode.com/problems/fraction-to-recurring-decimal/
# Runtime: 1 ms
# Memory: 53.5 MB

/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 * O(denominator) time, O(denominator) space - using HashMap to detect cycle
 */
var fractionToDecimal = function(numerator, denominator) {
    if (numerator === 0) return "0";
    
    let result = "";
    
    // Handle sign
    if ((numerator < 0) !== (denominator < 0)) {
        result = "-";
    }
    
    // Work with absolute values
    let num = Math.abs(numerator);
    let den = Math.abs(denominator);
    
    // Integer part
    result += Math.floor(num / den);
    let remainder = num % den;
    
    if (remainder === 0) return result;
    
    result += ".";
    
    // Decimal part - track remainders to find cycle
    const remainderMap = new Map();
    
    while (remainder !== 0) {
        if (remainderMap.has(remainder)) {
            const idx = remainderMap.get(remainder);
            return result.slice(0, idx) + "(" + result.slice(idx) + ")";
        }
        
        remainderMap.set(remainder, result.length);
        remainder *= 10;
        result += Math.floor(remainder / den);
        remainder %= den;
    }
    
    return result;
};