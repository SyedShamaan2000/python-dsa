# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Leetcode 128th problem: https://leetcode.com/problems/longest-consecutive-sequence/description/

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution1:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # brute-force
        arr = sorted(nums)
        prev = []
        next = []

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                continue
            elif arr[i] + 1 == arr[i + 1]:
                next.append(arr[i])
            else:
                prev.append(len(next) + 1)
                next = []

        if len(next) == 0 and len(prev) != 0:
            return max(max(prev), 1)
        elif len(prev) == 0:
            return len(next) + 1
        else:
            return max(max(prev), len(next) + 1)


class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        values = [1 for _ in nums]
        # print(values)
        nums_dict = dict(zip(nums, values))
        # print(nums_set)
        for n in nums_dict:
            if n - 1 in nums_dict:
                continue
            else:
                i = n
                while i + 1 in nums_dict:
                    nums_dict[n] += 1
                    i += 1

        # print(nums_set)
        return max(nums_dict.values())



class Solution3:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                length = 1
                while next_num in nums_set:
                    length += 1
                    next_num += 1
                longest = max(longest, length)

        return longest





arr1 = [100, 4, 200, 1, 3, 2]
arr2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
arr3 = [1, 0, 1, 2]
arr4 = [1, 2, 6, 7, 8]
arr5 = [1, 2, 6, 7, 8, 9, 22, 23, 24, 25, 26, 32, 33, 34, 35]
arr6 = [0, 0]

sol1 = Solution1()

# print(sol1.longestConsecutive(arr1))
# print(sol1.longestConsecutive(arr2))
# print(sol1.longestConsecutive(arr3))
# print(sol1.longestConsecutive(arr4))
# print(sol1.longestConsecutive(arr5))
# print(sol1.longestConsecutive(arr6))


sol2 = Solution2()

# print(sol2.longestConsecutive(arr1))
# print(sol2.longestConsecutive(arr2))
# print(sol2.longestConsecutive(arr3))
# print(sol2.longestConsecutive(arr4))
# print(sol2.longestConsecutive(arr5))
# print(sol2.longestConsecutive(arr6))

sol3 = Solution3()
print(sol3.longestConsecutive(arr1))
print(sol3.longestConsecutive(arr2))
print(sol3.longestConsecutive(arr3))
print(sol3.longestConsecutive(arr4))
print(sol3.longestConsecutive(arr5))
print(sol3.longestConsecutive(arr6))
