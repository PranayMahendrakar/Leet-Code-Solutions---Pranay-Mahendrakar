# Problem: Top K Frequent Elements
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 7 ms
# Memory: 22.8 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                return res[:k]
        