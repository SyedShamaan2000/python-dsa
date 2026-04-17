"""
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""


# LeetCode 28th problem - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def brute_force(self, needle: str, haystack: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def sliding_window(self, needle: str, haystack: str) -> int:
        n: int = len(haystack)
        m: int = len(needle)

        if m > n or m == 0:
            return -1

        # We slide a window of length m across the haystack
        for i in range(n - m + 1):
            # Python's slicing [i:i+m] acts like a window
            if haystack[i : i + m] == needle:
                return i

        return -1


sol = Solution()

print(sol.brute_force("small", "A smart small cat in a small town"))
# Time Complexity: O(n times m)
# Why? Internally, Python’s in operator and .index() method must scan the haystack (length n).
# In the worst case (e.g., haystack = "aaaaaab" and needle = "aaab"),
# it compares a portion of the needle (length m) at each position of the haystack.
# Most modern Python versions use a highly optimized version of the Boyer-Moore or Horspool algorithm,
# but the theoretical upper bound for this simple search remains O(n times m).
# Space Complexity: O(1)
# Why? It does not create any major auxiliary data structures that grow with the size of the input strings.
print(sol.sliding_window("small", "A smart small cat in a small town"))
# Time Complexity: O(n times m)
# Why?
# 1. The for loop runs exactly n - m + 1 times, which is roughly O(n).
# 2. Inside the loop, the slicing haystack[i : i + m] and
# the string comparison == needle both take O(m) time.
# 3. Multiplying these together gives us a total worst-case time of O((n - m) times m) approx O(n times m).
# Space Complexity: O(m)
# Why?
# In Python, string slicing (e.g., haystack[i : i + m]) creates a new copy of that substring in memory.
# Since that substring is the same length as the needle (m), the space complexity is O(m).
