# Problem: Reorder List
# Difficulty: Medium
# URL: https://leetcode.com/problems/reorder-list/
# Runtime: 2 ms
# Memory: 65.3 MB

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 * O(n) time, O(1) space - Find middle, reverse second half, merge
 */
var reorderList = function(head) {
    if (!head || !head.next) return;
    
    // Step 1: Find middle using slow/fast pointers
    let slow = head, fast = head;
    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Step 2: Reverse the second half
    let prev = null, curr = slow.next;
    slow.next = null; // Cut the list
    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    
    // Step 3: Merge two halves (first and reversed second)
    let first = head, second = prev;
    while (second) {
        const tmp1 = first.next;
        const tmp2 = second.next;
        first.next = second;
        second.next = tmp1;
        first = tmp1;
        second = tmp2;
    }
};