'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists
'''

class Solution:
    def twoSum(self, nums, target):
        seen_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_indices:
                return [seen_indices[complement], i]

            seen_indices[num] = i

        return []

# Example usage:
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
result1 = solution.twoSum(nums1, target1)
print(result1)  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
result2 = solution.twoSum(nums2, target2)
print(result2)  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
result3 = solution.twoSum(nums3, target3)
print(result3)  # Output: [0, 1]
