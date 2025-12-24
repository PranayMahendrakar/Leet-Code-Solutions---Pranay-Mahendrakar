# Problem: Clone Graph
# Difficulty: Medium
# URL: https://leetcode.com/problems/clone-graph/
# Runtime: 56 ms
# Memory: 57.4 MB

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;
    
    const visited = new Map();
    
    const dfs = (n) => {
        if (visited.has(n)) return visited.get(n);
        
        const clone = new _Node(n.val);
        visited.set(n, clone);
        
        for (const neighbor of n.neighbors) {
            clone.neighbors.push(dfs(neighbor));
        }
        
        return clone;
    };
    
    return dfs(node);
};