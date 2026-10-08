"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""

"""
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

# LeetCode 15th problem - https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSumBruteForce(self, nums: list[int]) -> list[list[int]]:
        seen = set()
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (
                        nums[i] + nums[j] + nums[k] == 0
                        and i != j
                        and j != k
                        and i != k
                        and tuple(sorted((nums[i], nums[j], nums[k]))) not in seen
                    ):
                        seen.add(tuple(sorted((nums[i], nums[j], nums[k]))))

        return [list(i) for i in seen]

    def threeSumHash(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()
        h = {}

        for i, num in enumerate(nums):
            h[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    result.add(tuple(sorted([nums[i], nums[j], desired])))

        return [list(i) for i in result]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1

        return answer


sol = Solution()

arr1 = [-1, 0, 1, 2, -1, -4]
arr2 = [0, 1, 1]
arr3 = [0, 0, 0]

# print(sol.threeSumBruteForce(arr1))
# print(sol.threeSumBruteForce(arr2))
# print(sol.threeSumBruteForce(arr3))

print(sol.threeSum(arr1))
