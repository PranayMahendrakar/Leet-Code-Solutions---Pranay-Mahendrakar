# Problem: Course Schedule
# Difficulty: Medium
# URL: https://leetcode.com/problems/course-schedule/
# Runtime: 10 ms
# Memory: 60.6 MB

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 * O(V+E) time, O(V+E) space - BFS Topological Sort (Kahn's Algorithm)
 */
var canFinish = function(numCourses, prerequisites) {
    const graph = Array.from({length: numCourses}, () => []);
    const inDegree = new Array(numCourses).fill(0);
    
    // Build graph and count in-degrees
    for (const [course, prereq] of prerequisites) {
        graph[prereq].push(course);
        inDegree[course]++;
    }
    
    // Start with courses that have no prerequisites
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }
    
    let completed = 0;
    
    while (queue.length > 0) {
        const course = queue.shift();
        completed++;
        
        for (const next of graph[course]) {
            inDegree[next]--;
            if (inDegree[next] === 0) queue.push(next);
        }
    }
    
    return completed === numCourses;
};