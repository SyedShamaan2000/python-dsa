"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container,
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

# LeetCode 11th problem - https://leetcode.com/problems/container-with-most-water/description/

# Example 1:
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    def maxAreaBruteForce(self, height: list[int]) -> int:
        n = len(height)
        max_value = 0

        for i in range(n):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                b = j - i
                max_value = max(max_value, h * b)

        return max_value

    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_value = 0

        l = 0
        r = n - 1

        while l < r:
            h = min(height[l], height[r])
            b = r - l
            max_value = max(max_value, h * b)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_value


arr1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
arr2 = [1, 1]

sol = Solution()

print(sol.maxAreaBruteForce(arr1))
print(sol.maxAreaBruteForce(arr2))
print(sol.maxArea(arr1))
print(sol.maxArea(arr2))
