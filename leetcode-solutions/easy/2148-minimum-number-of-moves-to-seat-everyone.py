# Problem: Minimum Number of Moves to Seat Everyone
# Difficulty: Easy
# URL: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
# Runtime: 3 ms
# Memory: 12.6 MB

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))