# Problem: Image Smoother
# Difficulty: Easy
# URL: https://leetcode.com/problems/image-smoother/
# Runtime: 238 ms
# Memory: 13.5 MB

class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1
                result[i][j] = total // count
        return result