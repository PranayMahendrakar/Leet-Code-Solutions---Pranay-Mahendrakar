# Problem: Remove Nth Node From End of List
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Runtime: 0 ms
# Memory: 12.6 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next