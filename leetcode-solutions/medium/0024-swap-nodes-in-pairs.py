# Problem: Swap Nodes in Pairs
# Difficulty: Medium
# URL: https://leetcode.com/problems/swap-nodes-in-pairs/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
        
        return dummy.next