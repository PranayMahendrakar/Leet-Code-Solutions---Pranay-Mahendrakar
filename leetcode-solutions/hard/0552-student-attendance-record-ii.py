# Problem: Student Attendance Record II
# Difficulty: Hard
# URL: https://leetcode.com/problems/student-attendance-record-ii/
# Runtime: 4012 ms
# Memory: 15.8 MB

class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7
        
        # dp[a][l] = count of valid records
        # a = 0 or 1 (count of A's), l = 0,1,2 (ending consecutive L's)
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Empty record: 0 A's, 0 ending L's
        
        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]
            
            for a in range(2):
                for l in range(3):
                    if dp[a][l] == 0:
                        continue
                    
                    # Add P: resets L count
                    new_dp[a][0] = (new_dp[a][0] + dp[a][l]) % MOD
                    
                    # Add L: if not already 2 consecutive L's
                    if l < 2:
                        new_dp[a][l + 1] = (new_dp[a][l + 1] + dp[a][l]) % MOD
                    
                    # Add A: if no A yet
                    if a == 0:
                        new_dp[1][0] = (new_dp[1][0] + dp[a][l]) % MOD
            
            dp = new_dp
        
        result = 0
        for a in range(2):
            for l in range(3):
                result = (result + dp[a][l]) % MOD
        return result