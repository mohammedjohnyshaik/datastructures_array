from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on whether the current_sum is less or greater than the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
# Example usage:
solution = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
target1 = 1
print(solution.threeSumClosest(nums1, target1))  # Output: 2

nums2 = [0, 1, 1]
target2 = 1
print(solution.threeSumClosest(nums2, target2))  # Output: 2

nums3 = [0, 0, 0]
target3 = 1
print(solution.threeSumClosest(nums3, target3))  # Output: 0
