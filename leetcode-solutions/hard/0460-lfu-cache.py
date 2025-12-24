# Problem: LFU Cache
# Difficulty: Hard
# URL: https://leetcode.com/problems/lfu-cache/
# Runtime: 390 ms
# Memory: 83.1 MB

class LFUCache:

    def __init__(self, capacity):
        from collections import defaultdict, OrderedDict
        self.capacity = capacity
        self.cache = {}  # key -> (value, freq)
        self.freq_map = defaultdict(OrderedDict)  # freq -> OrderedDict of keys
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        
        value, freq = self.cache[key]
        
        # Update frequency
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        self.freq_map[freq + 1][key] = None
        self.cache[key] = (value, freq + 1)
        
        return value

    def put(self, key, value):
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # Update frequency
            self.cache[key] = (value, self.cache[key][1])
            return
        
        if len(self.cache) >= self.capacity:
            # Remove least frequently used
            lfu_key = next(iter(self.freq_map[self.min_freq]))
            del self.freq_map[self.min_freq][lfu_key]
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
            del self.cache[lfu_key]
        
        self.cache[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1