# Problem: Contains Duplicate III
# Difficulty: Hard
# URL: https://leetcode.com/problems/contains-duplicate-iii/
# Runtime: 114 ms
# Memory: 25.6 MB

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False
        
        # Bucket sort approach - O(n) time
        bucket_size = valueDiff + 1  # +1 to handle valueDiff = 0
        buckets = {}
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            # Check same bucket
            if bucket_id in buckets:
                return True
            
            # Check adjacent buckets
            if bucket_id - 1 in buckets and num - buckets[bucket_id - 1] <= valueDiff:
                return True
            if bucket_id + 1 in buckets and buckets[bucket_id + 1] - num <= valueDiff:
                return True
            
            # Add current element to bucket
            buckets[bucket_id] = num
            
            # Remove element outside window
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket]
        
        return False