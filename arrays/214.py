"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# Leetcode 217th problem: https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_dict = {}
        for num in range(len(nums)):
            print(hash_dict)
            print(nums[num])
            if nums[num] in hash_dict:
                return True
            hash_dict[nums[num]] = num
        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
