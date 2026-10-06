class Solution(object):
    def countGroups(self, position, speed, distance):
        """
        :type position: List[int]
        :type speed: List[int]
        :type distance: int
        :rtype: int
        """
        n = len(position)
        count = 1
        lead_speed = speed[n - 1]  # speed of the nearest surviving group ahead
        for i in range(n - 2, -1, -1):
            if position[i + 1] - position[i] <= distance:
                continue  # merges at t = 0
            if speed[i] <= lead_speed:
                count += 1  # can never catch up, so it leads a new group
                lead_speed = speed[i]
        return count