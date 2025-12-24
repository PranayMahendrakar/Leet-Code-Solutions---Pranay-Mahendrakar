# Problem: Reverse Words in a String
# Difficulty: Medium
# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Runtime: 6 ms
# Memory: 56 MB

/**
 * @param {string} s
 * @return {string}
 * O(n) time, O(n) space
 */
var reverseWords = function(s) {
    const words = [];
    let i = 0;
    const n = s.length;
    
    while (i < n) {
        // Skip spaces
        while (i < n && s[i] === ' ') i++;
        if (i >= n) break;
        
        // Collect word
        let word = '';
        while (i < n && s[i] !== ' ') {
            word += s[i];
            i++;
        }
        words.push(word);
    }
    
    // Reverse words and join
    return words.reverse().join(' ');
};