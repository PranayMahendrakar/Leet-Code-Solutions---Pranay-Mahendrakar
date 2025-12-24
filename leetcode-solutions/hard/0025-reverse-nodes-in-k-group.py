# Problem: Reverse Nodes in k-Group
# Difficulty: Hard
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Runtime: 8 ms
# Memory: 14.1 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while count >= k:
            # Reverse k nodes
            group_start = prev_group_end.next
            prev = None
            curr = group_start
            
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect with previous group
            prev_group_end.next = prev
            group_start.next = curr
            prev_group_end = group_start
            
            count -= k
        
        return dummy.next