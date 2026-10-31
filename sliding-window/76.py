"""
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

"""


class Solution:
    def minWindowSlow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        t_dict = {}
        for i in range(n):
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        l = 0
        min_window = 10**6
        s_index = 0
        win_chars = {}

        def valid():
            for key in t_dict:
                if key not in win_chars or win_chars[key] < t_dict[key]:
                    return False
            return True

        for r in range(m):
            win_chars[s[r]] = 1 + win_chars.get(s[r], 0)

            while valid():
                w = r - l + 1
                if w < min_window:
                    s_index = l
                    min_window = w

                if win_chars[s[l]] == 1:
                    del win_chars[s[l]]
                else:
                    win_chars[s[l]] -= 1

                l += 1
        return s[s_index : min_window + s_index] if min_window != 10**6 else ""

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        t_dict = {}
        for i in range(n):
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        l = 0
        min_window = 10**6
        s_index = 0
        win_chars = {}

        have = 0
        need = len(t_dict)

        for r in range(m):
            win_chars[s[r]] = 1 + win_chars.get(s[r], 0)

            if s[r] in t_dict and win_chars[s[r]] == t_dict[s[r]]:
                have += 1

            while have == need:
                w = r - l + 1
                if w < min_window:
                    s_index = l
                    min_window = w

                if s[l] in t_dict and win_chars[s[l]] == t_dict[s[l]]:
                    have -= 1
                if win_chars[s[l]] == 1:
                    del win_chars[s[l]]
                else:
                    win_chars[s[l]] -= 1

                l += 1
        return s[s_index : min_window + s_index] if min_window != 10**6 else ""


sol = Solution()
s1 = "ADOBECODEBANC"
t1 = "ABC"
s2 = "a"
t2 = "a"
s3 = "a"
t3 = "aa"
s4 = "a"
t4 = "b"
print(sol.minWindowSlow(s1, t1))
print(sol.minWindowSlow(s4, t4))
print(sol.minWindow(s1, t1))
print(sol.minWindow(s4, t4))
