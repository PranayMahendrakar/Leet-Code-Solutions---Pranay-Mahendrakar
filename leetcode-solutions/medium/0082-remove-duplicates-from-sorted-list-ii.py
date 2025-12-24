# Problem: Remove Duplicates from Sorted List II
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Runtime: 6 ms
# Memory: 12.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                # Skip all nodes with same value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        
        return dummy.next