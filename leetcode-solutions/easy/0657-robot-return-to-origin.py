# Problem: Robot Return to Origin
# Difficulty: Easy
# URL: https://leetcode.com/problems/robot-return-to-origin/
# Runtime: 1 ms
# Memory: 17.7 MB

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')