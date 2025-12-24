# Problem: Min Stack
# Difficulty: Medium
# URL: https://leetcode.com/problems/min-stack/
# Runtime: 13 ms
# Memory: 65.8 MB

/**
 * O(1) time for all operations, O(n) space
 * Use two stacks: one for values, one for min values
 */
var MinStack = function() {
    this.stack = [];
    this.minStack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val);
    // Push to minStack if empty or val <= current min
    if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
        this.minStack.push(val);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    const val = this.stack.pop();
    // Pop from minStack if it matches
    if (val === this.minStack[this.minStack.length - 1]) {
        this.minStack.pop();
    }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minStack[this.minStack.length - 1];
};