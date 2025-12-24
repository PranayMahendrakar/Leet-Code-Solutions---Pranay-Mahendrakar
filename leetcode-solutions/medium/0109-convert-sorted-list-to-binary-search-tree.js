# Problem: Convert Sorted List to Binary Search Tree
# Difficulty: Medium
# URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Runtime: 4 ms
# Memory: 60.9 MB

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    if (!head) return null;
    if (!head.next) return new TreeNode(head.val);
    
    // Find middle using slow/fast pointers
    let slow = head, fast = head, prev = null;
    
    while (fast && fast.next) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Disconnect left half
    if (prev) prev.next = null;
    
    // slow is the middle node
    const root = new TreeNode(slow.val);
    
    // Build subtrees
    root.left = sortedListToBST(prev ? head : null);
    root.right = sortedListToBST(slow.next);
    
    return root;
};