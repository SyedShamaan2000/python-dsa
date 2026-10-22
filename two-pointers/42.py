"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

# Example 1:
# https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


class Solution:
    def trapBruteForce(self, height: list[int]) -> int:
        if not height:
            return 0
        trappedWater = 0
        n = len(height)
        print(n)
        left_arr = []
        right_arr = []
        max_left = 0
        max_right = 0

        for i in range(n):
            left_arr.append(max_left)
            max_left = max(max_left, height[i])
        for j in range(n - 1, -1, -1):
            right_arr.append(max_right)
            max_right = max(max_right, height[j])

        right_arr.reverse()

        print(height)
        print(left_arr)
        print(right_arr)

        for i in range(n):
            if min(left_arr[i], right_arr[i]) - height[i] > 0:
                trappedWater += min(left_arr[i], right_arr[i]) - height[i]

        return trappedWater

    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n - 1
        max_left = height[l]
        max_right = height[r]
        trapped_water = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                trapped_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped_water += max_right - height[r]
                

        return trapped_water


sol = Solution()

arr1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr2 = [4, 2, 0, 3, 2, 5]

# print(sol.trapBruteForce(arr1))
# print(sol.trapBruteForce(arr2))
print(sol.trap(arr1))
print(sol.trap(arr2))
