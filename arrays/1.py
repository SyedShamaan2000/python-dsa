"""
2Sum Problem
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to the target.
(OR)
Given a sorted array A (sorted in ascending order), having N integers,
find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
"""

# LeetCode 1st problem - https://leetcode.com/problems/two-sum/description/


# Example I have in my mind: array - [1, 3, 2, 6, 4], target - 9
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for num in range(len(nums)):
            if target - nums[num] in num_dict:
                return num_dict[target - nums[num]], num
            num_dict[nums[num]] = num


sol = Solution()
print(sol.twoSum([1, 3, 2, 6, 4], 9))
