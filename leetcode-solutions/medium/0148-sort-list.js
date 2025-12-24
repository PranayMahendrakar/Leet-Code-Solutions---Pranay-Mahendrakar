# Problem: Sort List
# Difficulty: Medium
# URL: https://leetcode.com/problems/sort-list/
# Runtime: 18 ms
# Memory: 78.3 MB

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if (!head || !head.next) return head;
    
    // Find middle
    let slow = head, fast = head, prev = null;
    while (fast && fast.next) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    prev.next = null;
    
    // Sort both halves
    const left = sortList(head);
    const right = sortList(slow);
    
    // Merge
    return merge(left, right);
};

function merge(l1, l2) {
    const dummy = new ListNode(0);
    let curr = dummy;
    
    while (l1 && l2) {
        if (l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
    }
    
    curr.next = l1 || l2;
    return dummy.next;
}