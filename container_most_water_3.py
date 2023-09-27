class Solution:
    def maxArea(self, height):
        max_area = 0
        n = len(height)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, dp[i][j])

        return max_area
solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solution.maxArea(height)
print(result)