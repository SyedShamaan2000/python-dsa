"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    # Array - slow!
    def characterReplacementArray(self, s: str, k: int) -> int:
        longest_substring = 0
        l = 0
        alpha_array = [0] * 26

        for r in range(len(s)):
            print(ord(s[r]))
            alpha_array[ord(s[r]) - 65] += 1
            print(alpha_array)
            while (r - l + 1) - max(alpha_array) > k:
                alpha_array[ord(s[l]) - 65] -= 1
                l += 1

            longest_substring = max(longest_substring, (r - l + 1))

        return longest_substring

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest


str1 = "ABAB"
k1 = 2
str2 = "AABABBA"
k2 = 1

sol = Solution()
print(sol.characterReplacement(str2, k2))
