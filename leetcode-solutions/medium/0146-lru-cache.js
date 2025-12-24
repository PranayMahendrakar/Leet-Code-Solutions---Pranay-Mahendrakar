# Problem: LRU Cache
# Difficulty: Medium
# URL: https://leetcode.com/problems/lru-cache/
# Runtime: 90 ms
# Memory: 107.7 MB

/**
 * @param {number} capacity
 * O(1) time for get and put using HashMap + Doubly Linked List
 */
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
    // Doubly linked list with dummy head and tail
    this.head = { key: 0, val: 0, prev: null, next: null };
    this.tail = { key: 0, val: 0, prev: null, next: null };
    this.head.next = this.tail;
    this.tail.prev = this.head;
};

LRUCache.prototype.removeNode = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

LRUCache.prototype.addToHead = function(node) {
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next.prev = node;
    this.head.next = node;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (!this.cache.has(key)) return -1;
    const node = this.cache.get(key);
    // Move to head (most recently used)
    this.removeNode(node);
    this.addToHead(node);
    return node.val;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.cache.has(key)) {
        const node = this.cache.get(key);
        node.val = value;
        this.removeNode(node);
        this.addToHead(node);
    } else {
        const newNode = { key, val: value, prev: null, next: null };
        this.cache.set(key, newNode);
        this.addToHead(newNode);
        if (this.cache.size > this.capacity) {
            // Remove LRU (tail.prev)
            const lru = this.tail.prev;
            this.removeNode(lru);
            this.cache.delete(lru.key);
        }
    }
};