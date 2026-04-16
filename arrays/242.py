# Leetcode 242nd problem: https://leetcode.com/problems/valid-anagram/description/

# Given: s and t consist of lowercase English letters.
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict


print(isAnagram("anagram", "nagaram"))
print(isAnagram("cat", "dog"))
print(isAnagram("aacc", "ccac"))
print(isAnagram("ab", "a"))
