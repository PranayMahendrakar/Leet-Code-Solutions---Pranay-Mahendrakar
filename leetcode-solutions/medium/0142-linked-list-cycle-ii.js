# Problem: Linked List Cycle II
# Difficulty: Medium
# URL: https://leetcode.com/problems/linked-list-cycle-ii/
# Runtime: 48 ms
# Memory: 58 MB

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let slow = head, fast = head;
    
    // Detect cycle using Floyd's algorithm
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        
        if (slow === fast) {
            // Cycle found, find entry point
            let entry = head;
            while (entry !== slow) {
                entry = entry.next;
                slow = slow.next;
            }
            return entry;
        }
    }
    
    return null;
};