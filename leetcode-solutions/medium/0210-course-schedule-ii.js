# Problem: Course Schedule II
# Difficulty: Medium
# URL: https://leetcode.com/problems/course-schedule-ii/
# Runtime: 14 ms
# Memory: 60.1 MB

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 * O(V+E) time, O(V+E) space - BFS Topological Sort
 */
var findOrder = function(numCourses, prerequisites) {
    const graph = Array.from({length: numCourses}, () => []);
    const inDegree = new Array(numCourses).fill(0);
    
    // Build graph
    for (const [course, prereq] of prerequisites) {
        graph[prereq].push(course);
        inDegree[course]++;
    }
    
    // Start with courses that have no prerequisites
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }
    
    const order = [];
    
    while (queue.length > 0) {
        const course = queue.shift();
        order.push(course);
        
        for (const next of graph[course]) {
            inDegree[next]--;
            if (inDegree[next] === 0) queue.push(next);
        }
    }
    
    return order.length === numCourses ? order : [];
};