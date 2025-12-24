# Problem: Binary Search Tree Iterator
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-search-tree-iterator/
# Runtime: 10 ms
# Memory: 69 MB

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * O(1) average for next(), O(h) space using stack
 */
var BSTIterator = function(root) {
    this.stack = [];
    this.pushLeft(root);
};

BSTIterator.prototype.pushLeft = function(node) {
    while (node) {
        this.stack.push(node);
        node = node.left;
    }
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function() {
    const node = this.stack.pop();
    this.pushLeft(node.right);
    return node.val;
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function() {
    return this.stack.length > 0;
};