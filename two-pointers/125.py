"""
A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

# LeetCode 125th problem - https://leetcode.com/problems/valid-palindrome/description/

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(
            char for char in s if char.isalpha() or char.isalnum()
        ).lower()
        print(cleaned_str)
        print(cleaned_str[::-1])
        return cleaned_str == cleaned_str[::-1]

    def isPalindromeTwoPointers(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()

        while l <= r:
            if not (s[l].isalpha() or s[l].isalnum()):
                l += 1
            elif not (s[r].isalnum() or s[r].isalpha()):
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True


sol = Solution()

str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"
str3 = " "
str4 = "0P"

print(sol.isPalindrome(str1))
print(sol.isPalindrome(str2))
print(sol.isPalindrome(str3))
print(sol.isPalindrome(str4))
