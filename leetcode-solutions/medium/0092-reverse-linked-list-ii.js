# Problem: Reverse Linked List II
# Difficulty: Medium
# URL: https://leetcode.com/problems/reverse-linked-list-ii/
# Runtime: 0 ms
# Memory: 53.6 MB

/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (!head || left === right) return head;
    
    const dummy = new ListNode(0, head);
    let prev = dummy;
    
    // Move prev to the node before left
    for (let i = 1; i < left; i++) {
        prev = prev.next;
    }
    
    // Reverse the sublist
    let curr = prev.next;
    for (let i = 0; i < right - left; i++) {
        const next = curr.next;
        curr.next = next.next;
        next.next = prev.next;
        prev.next = next;
    }
    
    return dummy.next;
};