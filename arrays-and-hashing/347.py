# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Leetcode problem link: https://leetcode.com/problems/top-k-frequent-elements/
# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

from time_decorator import time_decorator
from typing import List

class Solution:
    @time_decorator
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency dictionary to count occurrences of each number
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        # Sort the items of the frequency dictionary based on frequency in descending order
        print(frequency_dict)
        print(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))
        # key=lambda item: item[1] means we are sorting based on the frequency (the second item in the tuple)
        # reverse=True means we want the highest frequency first
        sorted_items = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)

        # Extract the top k elements based on frequency
        top_k_elements = [item[0] for item in sorted_items[:k]]

        return top_k_elements


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(result)  # Output: [1, 2]