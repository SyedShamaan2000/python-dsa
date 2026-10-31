"""
Given two strings s1 and s2,
return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusionSlow(self, s1: str, s2: str) -> bool:
        # Slow
        s1_dict = {}
        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)

        l = 0

        while l < len(s2):
            r = min(l + len(s1), len(s2))
            print(l, r)
            s2_dict = {}
            for j in range(l, r):
                s2_dict[s2[j]] = 1 + s2_dict.get(s2[j], 0)
            print(s2_dict)
            if s1_dict == s2_dict:
                return True
            else:
                l += 1

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_array = [0] * 26
        s2_array = [0] * 26

        for i in range(len(s1)):
            s1_array[ord(s1[i]) - 97] += 1
            s2_array[ord(s2[i]) - 97] += 1

        if s1_array == s2_array:
            return True

        for i in range(len(s1), len(s2)):
            s2_array[ord(s2[i]) - 97] += 1
            s2_array[ord(s2[i - len(s1)]) - 97] -= 1
            if s1_array == s2_array:
                return True

        return False


sol = Solution()

s11 = "ab"
s21 = "eidbaooo"
s12 = "ab"
s22 = "eidboaoo"
s13 = "hello"
s23 = "ooolleoooleh"

# print(sol.checkInclusionSlow(s11, s21))
# print(sol.checkInclusionSlow(s12, s22))
# print(sol.checkInclusionSlow(s13, s23))


print(sol.checkInclusion(s12, s22))
print(sol.checkInclusion(s13, s23))
