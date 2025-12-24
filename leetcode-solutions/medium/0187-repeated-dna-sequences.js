# Problem: Repeated DNA Sequences
# Difficulty: Medium
# URL: https://leetcode.com/problems/repeated-dna-sequences/
# Runtime: 17 ms
# Memory: 62.5 MB

/**
 * @param {string} s
 * @return {string[]}
 * O(n) time, O(n) space - Sliding window with HashSet
 */
var findRepeatedDnaSequences = function(s) {
    if (s.length <= 10) return [];
    
    const seen = new Set();
    const result = new Set();
    
    for (let i = 0; i <= s.length - 10; i++) {
        const seq = s.substring(i, i + 10);
        if (seen.has(seq)) {
            result.add(seq);
        }
        seen.add(seq);
    }
    
    return Array.from(result);
};