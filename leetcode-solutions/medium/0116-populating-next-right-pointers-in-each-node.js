# Problem: Populating Next Right Pointers in Each Node
# Difficulty: Medium
# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Runtime: 48 ms
# Memory: 60 MB

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    if (!root) return null;
    
    let leftmost = root;
    
    // Level by level using next pointers (O(1) space)
    while (leftmost.left) {
        let curr = leftmost;
        
        while (curr) {
            // Connect left to right within same parent
            curr.left.next = curr.right;
            
            // Connect right to next parent's left
            if (curr.next) {
                curr.right.next = curr.next.left;
            }
            
            curr = curr.next;
        }
        
        leftmost = leftmost.left;
    }
    
    return root;
};