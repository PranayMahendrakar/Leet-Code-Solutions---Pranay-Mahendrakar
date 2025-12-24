# Problem: Implement Trie (Prefix Tree)
# Difficulty: Medium
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/
# Runtime: 46 ms
# Memory: 73.2 MB

var Trie = function() {
    this.root = {};
};

/** 
 * @param {string} word
 * @return {void}
 * O(m) time, O(m) space where m is word length
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for (const char of word) {
        if (!node[char]) node[char] = {};
        node = node[char];
    }
    node.isEnd = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 * O(m) time, O(1) space
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for (const char of word) {
        if (!node[char]) return false;
        node = node[char];
    }
    return node.isEnd === true;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 * O(m) time, O(1) space
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (const char of prefix) {
        if (!node[char]) return false;
        node = node[char];
    }
    return true;
};