# Problem: Apple Redistribution into Boxes
# Difficulty: Easy
# URL: https://leetcode.com/problems/apple-redistribution-into-boxes/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        current_capacity = 0
        for i, cap in enumerate(capacity):
            current_capacity += cap
            if current_capacity >= total_apples:
                return i + 1
        return len(capacity)