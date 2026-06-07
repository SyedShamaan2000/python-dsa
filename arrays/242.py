# Leetcode 242nd problem: https://leetcode.com/problems/valid-anagram/description/

# Given: s and t consist of lowercase English letters.
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict


def isAnagramWithDict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    return count_s == count_t


print(isAnagram("anagram", "nagaram"))
print(isAnagram("cat", "dog"))
print(isAnagram("aacc", "ccac"))
print(isAnagram("ab", "a"))

print(isAnagramWithDict("anagram", "nagaram"))
print(isAnagramWithDict("cat", "dog"))
print(isAnagramWithDict("aacc", "ccac"))
print(isAnagramWithDict("ab", "a"))