"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

# Leetcode 49th problem: https://leetcode.com/problems/group-anagrams/description/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from time_decorator import time_decorator


class Solution:
    @time_decorator
    def bruteForce(self, strs: list[str]) -> list[list[str]]:
        groups: list[list[str]] = []

        for word in strs:
            placed = False
            for group in groups:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    placed = True
                    break
            if not placed:
                groups.append([word])

        return groups

    @time_decorator
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = {}

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]

        return list(groups.values())


sol = Solution()
print(sol.bruteForce(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
