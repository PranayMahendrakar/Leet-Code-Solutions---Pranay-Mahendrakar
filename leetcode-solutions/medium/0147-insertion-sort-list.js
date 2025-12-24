# Problem: Insertion Sort List
# Difficulty: Medium
# URL: https://leetcode.com/problems/insertion-sort-list/
# Runtime: 29 ms
# Memory: 59.2 MB

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 * O(n²) time, O(1) space - Insertion sort optimized
 */
var insertionSortList = function(head) {
    if (!head || !head.next) return head;
    
    const dummy = new ListNode(0);
    let curr = head;
    
    while (curr) {
        const next = curr.next;
        
        // Find insert position in sorted list
        let prev = dummy;
        while (prev.next && prev.next.val < curr.val) {
            prev = prev.next;
        }
        
        // Insert curr after prev
        curr.next = prev.next;
        prev.next = curr;
        
        curr = next;
    }
    
    return dummy.next;
};