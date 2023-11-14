from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            left, right = i+1, len(nums)-1
            target = -nums[i]
            while left<right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result

# Example usage:
solution = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]
nums2 = [0, 1, 1]
print(solution.threeSum(nums2))  # Output: []
nums3 = [0, 0, 0]
print(solution.threeSum(nums3))  # Output: [[0, 0, 0]]