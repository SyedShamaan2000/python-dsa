"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

# LeetCode 3rd problem - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def brute_force(s: str) -> int:
        if not s:
            return 0

        n: int = len(s)
        max_len = 1

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len: int = max(max_len, j - i + 1)

        return max_len

    def sliding_window(s: str) -> int:
        if not s:
            return 0
        char_index = {}  # maps char -> its most recent index
        max_len = 0
        l = 0  # left boundary of the window

        for r, char in enumerate(s):
            # If char was seen AND it's inside our current window
            if char in char_index and char_index[char] >= l:
                print(char_index, char_index[char])
                l = char_index[char] + 1  # shrink: move left past the duplicate

            char_index[char] = r  # update char's latest position
            max_len = max(max_len, r - l + 1)

        return max_len


sol = Solution
print(sol.brute_force("pprpewskwyt"))
print(sol.brute_force("abcabcbb"))
# Time Complexity:  O(n^2)
# Why? Two nested loops - outer picks start, inner expands right.
# Space Complexity: O(min(n, a)) where a = alphabet size
# Why? The `seen` set holds at most the number of unique chars.
# The Inefficiency: When we find "abc" starting at i=0 and hit a duplicate at i=3,
#                   we throw away everything and restart from i=1. That's wasteful —
#                   we already KNOW 'a' is in our window!
print(sol.sliding_window("pprpewskwyt"))
print(sol.sliding_window("abcabcbb"))
# Time Complexity:  O(n)
# Why? Single pass — r visits each char once; l only moves forward.
# Space Complexity: O(min(n, a))
# Why? char_index holds at most `a` entries (alphabet size, e.g. 128 for ASCII).
# Improvement: O(n²) → O(n) in time; space stays the same but is tightly bounded.
