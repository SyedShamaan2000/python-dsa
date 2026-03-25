"""
Given an integer array nums sorted in non-decreasing order (basically means in ascending order but can have duplicates),
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k.
After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.
"""

# LeetCode 26th problem - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Assuming an integer array [-4, -2, -2, -1, 0, 0, 4, 4, 7, 9]
# unique elements (k) = 7
# expects: [-4, -2, -1, 0, 4, 7, 9, _, _, ...], ignores after k (7th position)


class Solution:
    def brute_force(self, nums: list) -> tuple[int, list]:
        unique_elements: list = []
        for x in nums:
            if x not in unique_elements:
                unique_elements.append(x)

        # Manually overwrite the original list
        for i in range(len(unique_elements)):
            nums[i] = unique_elements[i]

        return len(unique_elements), nums

    def two_pointers(self, nums: list) -> tuple[int, list]:
        left: int = 1

        for r in range(1, len(nums) - (left - 1)):
            if nums[r] != nums[r - 1]:
                nums[left] = nums[r]
                left += 1

        return left, nums


sol = Solution()

print(sol.brute_force([-4, -2, -2, -1, 0, 0, 4, 4, 7, 9]))
# Time Complexity: O(n^2)
# Why? The line if x not in unique_elements performs a linear scan on unique_elements for every element in nums.
# Space Complexity: O(n)
# Why? We are storing unique elements in a separate list.
# The Inefficiency: We aren't taking advantage of the fact that the input is already sorted.
# In a sorted list, duplicates are always next to each other!


print(sol.two_pointers([-4, -2, -2, -1, 0, 0, 4, 4, 7, 9]))
# Time Complexity: O(n)
# Why? We iterate through the list exactly once.
# Space Complexity: O(1)
# Why? We define left variable
