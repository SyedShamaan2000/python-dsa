# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# LeetCode: 238. Product of Array Except Self : https://leetcode.com/problems/product-of-array-except-self/description/


from time_decorator import time_decorator


class Solution:
    @time_decorator
    def brute_force(self, nums: list) -> list:
        n = len(nums)
        answer = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:  # skip the current index
                    product *= nums[j]
            answer.append(product)

        return answer

    @time_decorator
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Solution with less than O(n) time complexity and without using division operation
        n = len(nums)
        answer = [1] * n  # will hold prefix products first, then final answer

        # Pass 1: fill answer[i] with product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            print(f"Index {i}: prefix={prefix}, nums[i]={nums[i]}")
            answer[i] = prefix  # everything before i, multiplied so far
            print(f"answer[{i}] after prefix assignment: {answer[i]}")
            prefix *= nums[i]  # now include nums[i] for the next index
            print(f"Updated prefix after including nums[{i}]: {prefix}")

        print("After Pass 1 (Prefix Products):", answer)

        # Pass 2: multiply in the product of everything to the RIGHT of i
        suffix = 1
        # Why n - 1 to -1? Because we want to iterate backwards from the last index to the first index (0).
        for i in range(n - 1, -1, -1):  # walk backwards from last index to 0
            print(f"Index {i}: suffix={suffix}, nums[i]={nums[i]}")
            answer[i] *= suffix  # combine existing left-product with right-product
            print(f"answer[{i}] after combining with suffix: {answer[i]}")
            suffix *= nums[i]  # now include nums[i] for the next index (moving left)
            print(f"Updated suffix after including nums[{i}]: {suffix}")

        print("After Pass 2 (Final Answer):", answer)
        return answer


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print("Brute Force Result:", solution.brute_force(nums))
    print("Optimized Result:", solution.productExceptSelf(nums))
    nums2 = [4, 5, 6]
    print("Optimized Result for nums2:", solution.productExceptSelf(nums2))
