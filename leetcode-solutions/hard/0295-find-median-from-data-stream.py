# Problem: Find Median from Data Stream
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-median-from-data-stream/
# Runtime: 815 ms
# Memory: 35.8 MB

class MedianFinder(object):

    def __init__(self):
        import heapq
        # Max heap for smaller half (negate values)
        self.small = []
        # Min heap for larger half
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        import heapq
        
        # Add to max heap (negate for max heap behavior)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Ensure size property: len(small) == len(large) or len(small) == len(large) + 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0