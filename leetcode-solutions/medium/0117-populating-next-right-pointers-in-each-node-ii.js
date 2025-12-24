# Problem: Populating Next Right Pointers in Each Node II
# Difficulty: Medium
# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Runtime: 47 ms
# Memory: 58.3 MB

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    if (!root) return null;
    
    let curr = root;
    
    while (curr) {
        let dummy = new Node(0);
        let tail = dummy;
        
        // Process current level
        while (curr) {
            if (curr.left) {
                tail.next = curr.left;
                tail = tail.next;
            }
            if (curr.right) {
                tail.next = curr.right;
                tail = tail.next;
            }
            curr = curr.next;
        }
        
        // Move to next level
        curr = dummy.next;
    }
    
    return root;
};