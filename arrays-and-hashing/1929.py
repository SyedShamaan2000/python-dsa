# Leetcode 1929th problem: https://leetcode.com/problems/concatenation-of-array/description/


def getConcatenation(nums: list[int]) -> list[int]:
    ans: list[int] = [0] * (2 * len(nums))
    for num in range(len(nums)):
        ans[num], ans[num + len(nums)] = nums[num], nums[num]
    return ans


print(getConcatenation([1, 2, 1]))
