# Problem: Count of Smaller Numbers After Self
# Difficulty: Hard
# URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Runtime: 1990 ms
# Memory: 42 MB

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        # Store (value, original index)
        indexed = [(nums[i], i) for i in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Merge and count
            merged = []
            i = j = 0
            right_count = 0  # Count of right elements that went before current left element
            
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    right_count += 1
                    merged.append(right[j])
                    j += 1
                else:
                    result[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
            
            while i < len(left):
                result[left[i][1]] += right_count
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(indexed)
        return result