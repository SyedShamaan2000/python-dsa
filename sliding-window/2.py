"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

# LeetCode 219th problem - https://leetcode.com/problems/contains-duplicate-ii/description/


class Solution:
    # Method rejected
    def brute_force_using_for_loop(arr, k) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                print(
                    f"Comparing: arr[{i}]={arr[i]} and arr[{j}]={arr[j]} (dist: {abs(i - j)})"
                )
                if arr[i] == arr[j] and (abs(i - j) <= k):
                    return True

        return False

    # Method rejected
    def brute_force_using_while_loop(arr, k) -> bool:
        n: int = len(arr)
        i = 0
        j: int = i + 1
        while i < n:
            while (j < n) and (abs(i - j) <= k):
                print(
                    f"Comparing: arr[{i}]={arr[i]} and arr[{j}]={arr[j]} (dist: {abs(i - j)})"
                )
                if arr[i] == arr[j]:
                    return True
                j += 1
            i += 1
            j = i + 1

        return False

    def sliding_window(arr, k) -> bool:
        window = set()

        for i in range(len(arr)):
            if arr[i] in window:
                return True
            else:
                window.add(arr[i])

            if len(window) > k:
                print(arr[i - k])
                window.remove(arr[i - k])
                print(window)

        return False


sol = Solution

print(sol.brute_force_using_for_loop([1, 2, 3, 1, 2, 3], 2))
# Time Complexity: O(n²)
# Why? Two nested loops — the outer runs n times and the inner runs up to n times per iteration,
# comparing every possible pair (i, j) in the array.
# Space Complexity: O(1)
# Why? No extra data structures are used; only a fixed number of index variables.
# The Inefficiency: We re-examine pairs we've already seen and check distances we could prune early.

print(sol.brute_force_using_while_loop([1, 2, 3, 1, 2, 3], 2))
# Time Complexity: O(n × k)
# Why? The outer while loop runs n times.
# The inner while loop runs at most k times per outer iteration
# (constrained by abs(i - j) <= k), giving O(n × k) total comparisons.
# In the worst case where k ≈ n, this degrades to O(n²).
# Space Complexity: O(1)
# Why? Only index variables i and j are used — no auxiliary data structures.
# The Inefficiency: We still scan up to k neighbours for every element;
# we're not reusing any information from the previous window position.

print(sol.sliding_window([1, 2, 3, 1, 2, 3, 4], 2))
# Time Complexity: O(n)
# Why? A single pass over the array — each element is added to and removed from
# the set at most once, making every set operation O(1) on average.
# Space Complexity: O(k)
# Why? The sliding window (set) holds at most k + 1 elements at any point in time,
# so memory usage is bounded by the window size k, not the full array length n.
