# Problem: Basic Calculator II
# Difficulty: Medium
# URL: https://leetcode.com/problems/basic-calculator-ii/
# Runtime: 23 ms
# Memory: 59.9 MB

/**
 * @param {string} s
 * @return {number}
 * O(n) time, O(1) space - No stack needed
 */
var calculate = function(s) {
    let result = 0, lastNum = 0, currentNum = 0;
    let operation = '+';
    
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        
        if (char >= '0' && char <= '9') {
            currentNum = currentNum * 10 + parseInt(char);
        }
        
        if ((char !== ' ' && isNaN(char)) || i === s.length - 1) {
            if (operation === '+') {
                result += lastNum;
                lastNum = currentNum;
            } else if (operation === '-') {
                result += lastNum;
                lastNum = -currentNum;
            } else if (operation === '*') {
                lastNum = lastNum * currentNum;
            } else if (operation === '/') {
                lastNum = Math.trunc(lastNum / currentNum);
            }
            operation = char;
            currentNum = 0;
        }
    }
    
    return result + lastNum;
};