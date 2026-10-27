"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

# LeetCode 121th problem - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfitBruteForce(self, prices: list[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n - 1):
                if prices[j] - prices[i] > 0:
                    profit = max(profit, prices[j] - prices[i])

        return profit

    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        n = len(prices)
        l = 0
        l_min = prices[0]

        while l < n:
            l_min = min(l_min, prices[l])
            if prices[l] - l_min > 0:
                profit = max(profit, prices[l] - l_min)
            l += 1

        return profit


arr1 = [7, 1, 5, 3, 6, 4]
arr2 = [7, 6, 4, 3, 1]

sol = Solution()

print(sol.maxProfitBruteForce(arr1))
print(sol.maxProfitBruteForce(arr2))
print(sol.maxProfit(arr1))
print(sol.maxProfit(arr2))
