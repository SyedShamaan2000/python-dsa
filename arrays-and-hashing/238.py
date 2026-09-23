"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.s
"""

# LeetCode 238th problem - https://leetcode.com/problems/product-of-array-except-self/description/

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        suffix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        for j in range(n - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]

        return answer


sol = Solution()

arr1 = [1, 2, 3, 4]
arr2 = [-1, 1, 0, -3, 3]

print(sol.productExceptSelf(arr1))
