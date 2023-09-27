class Solution:
    def maxArea(self, height):
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                max_area = max(max_area, area)
        return max_area

solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solution.maxArea(height)
print(result)
