"""
2Sum Problem
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to the target.
(OR)
Given a sorted array A (sorted in ascending order), having N integers,
find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
"""

# LeetCode 1st problem - https://leetcode.com/problems/two-sum/description/


# Example I have in my mind: array - [1, 3, 2, 6, 4], target - 9
class Solution:
    # Brute Force
    def two_sum_bf(self, nums: list[int], target: int) -> dict:
        # Iterate through each number in the list
        for i in range(len(nums)):
            # For each number, check every subsequent number
            for j in range(i + 1, len(nums)):
                # If they add up to the target, we found our pair!
                if nums[i] + nums[j] == target:
                    return {"elements": [nums[i], nums[j]], "indices": [i, j]}

    # Two pointers
    def two_sum_tp(self, nums: list[int], target: int) -> dict:
        # Create a list of pairs: (value, original_index)
        # This ensures we don't lose the position after sorting.
        indexed_nums: list = []
        for i, val in enumerate(nums):
            indexed_nums.append((val, i))
        # print(indexed_nums) # [(1, 0), (3, 1), (2, 2), (6, 3), (4, 4)]
        # Sort the list based on the values
        indexed_nums.sort()  # Python's Timsort is O(n log n)
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            current_sum: int = indexed_nums[left][0] + indexed_nums[right][0]

            if current_sum == target:
                # Return the original indices we stored earlier
                return {
                    "elements": [indexed_nums[left][0], indexed_nums[right][0]],
                    "indices": [indexed_nums[left][1], indexed_nums[right][1]],
                }

            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum

    # Using HashMap
    def two_sum_hm(self, nums, target) -> dict:
        # map to store: {value: original_index}
        seen: dict = {}

        # enumerate gives us both the index (i) and the value (n)
        for i, val in enumerate(nums):
            complement: int = target - val

            # Check if the number we need is already in our dictionary
            if complement in seen:
                # If found, return the index of the complement and current index
                return {
                    "elements": [nums[seen[complement]], nums[i]],
                    "indices": [seen[complement], i],
                }

            # If not found, add the current number and its index to the map
            seen[val] = i


sol = Solution()


print(sol.two_sum_bf(nums=[1, 3, 2, 6, 4], target=9))
# Time Complexity: O(n^2)
# Why? We have a loop inside a loop.
# For every element n, we potentially look at n-1 other elements.
# As the list grows, the time taken grows quadratically.
# Space Complexity: O(1)
# Why? We aren't using any extra storage that grows with the input size;
# we're just using a couple of index variables.


print(sol.two_sum_tp(nums=[1, 3, 2, 6, 4], target=9))
# Time Complexity: O(n log n)
# Why? Even though the pointer movement is O(n),
# the sorting step takes O(n log n) time.
# This is still much faster than the O(n^2) brute force for large lists!
# Space Complexity: O(n)
# Why? We created a new list indexed_nums to store the values and their original positions,
# which takes space proportional to the input size.
# Key Takeaways:
# Sorted Data is Key: The Two Pointers approach is a powerhouse,
# but it almost always requires the data to be sorted.
# If the data isn't sorted, sorting it first becomes your "bottleneck."
# Directional Logic: Moving pointers inward works because we have a guarantee that
# moving left only increases the sum and moving right only decreases it.


print(sol.two_sum_hm(nums=[1, 3, 2, 6, 4], target=9))
# Time Complexity: O(n)
# Why? We traverse the list containing n elements only once.
# Each lookup in the dictionary happens in O(1) time on average.
# Space Complexity: O(n)
# Why? In the worst case (where the matching pair is at the very end),
# we store n-1 elements in the dictionary.
# Key Takeaways:
# Trade-offs: This is a classic example of Space-Time Trade-off.
# We used extra memory (the dictionary) to gain massive speed.
# The "Complement" Pattern: Whenever you are looking for a pair that satisfies a relationship (like a sum or difference),
# ask: "What value am I missing, and have I seen it before?"
# One-Pass vs. Two-Pass: Notice we added the number to the dictionary after checking for the complement.
# This prevents us from using the same element twice (e.g., if target is 4 and the number is 2, it won't match with itself).
