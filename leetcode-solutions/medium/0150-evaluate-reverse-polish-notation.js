# Problem: Evaluate Reverse Polish Notation
# Difficulty: Medium
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Runtime: 5 ms
# Memory: 57.3 MB

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    const ops = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => Math.trunc(a / b)
    };
    
    for (const token of tokens) {
        if (ops[token]) {
            const b = stack.pop();
            const a = stack.pop();
            stack.push(ops[token](a, b));
        } else {
            stack.push(parseInt(token));
        }
    }
    
    return stack[0];
};