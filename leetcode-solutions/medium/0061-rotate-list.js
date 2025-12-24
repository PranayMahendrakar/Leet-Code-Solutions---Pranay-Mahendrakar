# Problem: Rotate List
# Difficulty: Medium
# URL: https://leetcode.com/problems/rotate-list/
# Runtime: 1 ms
# Memory: 56.5 MB

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (!head || !head.next || k === 0) return head;
    
    // Find length and tail
    let len = 1;
    let tail = head;
    while (tail.next) {
        len++;
        tail = tail.next;
    }
    
    // Optimize k
    k = k % len;
    if (k === 0) return head;
    
    // Find new tail (len - k - 1 steps from head)
    let newTail = head;
    for (let i = 0; i < len - k - 1; i++) {
        newTail = newTail.next;
    }
    
    // Rotate
    let newHead = newTail.next;
    newTail.next = null;
    tail.next = head;
    
    return newHead;
};