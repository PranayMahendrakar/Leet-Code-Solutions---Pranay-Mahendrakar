# Problem: Restore IP Addresses
# Difficulty: Medium
# URL: https://leetcode.com/problems/restore-ip-addresses/
# Runtime: 3 ms
# Memory: 54.7 MB

/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const result = [];
    
    const isValid = (str) => {
        if (str.length > 1 && str[0] === '0') return false;
        const num = parseInt(str);
        return num >= 0 && num <= 255;
    };
    
    const backtrack = (start, parts) => {
        if (parts.length === 4) {
            if (start === s.length) {
                result.push(parts.join('.'));
            }
            return;
        }
        
        for (let len = 1; len <= 3; len++) {
            if (start + len > s.length) break;
            const part = s.substring(start, start + len);
            if (isValid(part)) {
                parts.push(part);
                backtrack(start + len, parts);
                parts.pop();
            }
        }
    };
    
    backtrack(0, []);
    return result;
};