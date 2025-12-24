# Problem: Number of Nodes in the Sub-Tree With the Same Label
# Difficulty: Medium
# URL: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
# Runtime: 455 ms
# Memory: 112 MB

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        result = [0] * n
        
        def dfs(node, parent):
            count = [0] * 26
            label_idx = ord(labels[node]) - ord('a')
            count[label_idx] = 1
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    child_count = dfs(neighbor, node)
                    for i in range(26):
                        count[i] += child_count[i]
            
            result[node] = count[label_idx]
            return count
        
        dfs(0, -1)
        return result