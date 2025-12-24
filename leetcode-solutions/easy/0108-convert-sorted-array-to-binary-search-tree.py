# Problem: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Runtime: 3 ms
# Memory: 15.3 MB

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root