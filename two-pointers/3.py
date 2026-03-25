"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums
contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

# LeetCode 27th problem - https://leetcode.com/problems/remove-element/description/

array_nums: list = [-3, -9, -9, -2, -2, -3, 0, 2, 1, 5, 12, 1, 2, 2, 5]
integer_val: int = -2
# Expected -> no. of elements in nums which are not equal to -2, --> 13
# k: int = 13
# modify nums to [-3, -9, -9, -3, 0, 2, 1, 5, 12, 1, 2, 2, 5, -2, -2]


class Solution:
    def brute_force(self, nums: list, val: int) -> dict:
        i: int = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return {"nums": nums, "k": len(nums)}

    def swap_method(self, nums: list, val: int) -> dict:
        i: int = 0
        n: int = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return {"nums": nums, "k": n}


sol = Solution()

print(sol.brute_force([0, 1, 2, 2, 3, 0, 4, 2], 2))
# Time Complexity: O(n^2)???
# Why? The while loop runs n times.
# Inside, nums.remove() is itself an O(n) ??? operation because it has to search for the value
# and then shift every element to its right one position to the left. n times n = n^2 ???
# Space Complexity: O(1)
# Why? You are modifying the list in-place.
# The Inefficiency: Every time we find val, we potentially move thousands of other numbers.
# Since the order doesn't matter, we can avoid the "shifting" entirely.

print(sol.swap_method([0, 1, 2, 2, 3, 0, 4, 2], 2))
# Time Complexity: O(n)
# Why? Each element is visited at most once.
# The total number of operations is proportional to the length of the array.
# Space Complexity: O(1)
# Why? We only used two integer variables (i and n).
