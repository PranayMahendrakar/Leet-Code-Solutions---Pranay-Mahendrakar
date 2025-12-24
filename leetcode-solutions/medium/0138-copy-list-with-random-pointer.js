# Problem: Copy List with Random Pointer
# Difficulty: Medium
# URL: https://leetcode.com/problems/copy-list-with-random-pointer/
# Runtime: 43 ms
# Memory: 55.6 MB

/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 * O(n) time, O(1) space - Interweaving approach
 */
var copyRandomList = function(head) {
    if (!head) return null;
    
    // Step 1: Create cloned nodes and interweave them
    // Original: A -> B -> C becomes A -> A' -> B -> B' -> C -> C'
    let curr = head;
    while (curr) {
        const clone = new _Node(curr.val, curr.next, null);
        curr.next = clone;
        curr = clone.next;
    }
    
    // Step 2: Assign random pointers for cloned nodes
    curr = head;
    while (curr) {
        if (curr.random) {
            curr.next.random = curr.random.next;
        }
        curr = curr.next.next;
    }
    
    // Step 3: Separate the two lists
    const dummy = new _Node(0);
    let cloneCurr = dummy;
    curr = head;
    while (curr) {
        cloneCurr.next = curr.next;
        cloneCurr = cloneCurr.next;
        curr.next = curr.next.next;
        curr = curr.next;
    }
    
    return dummy.next;
};