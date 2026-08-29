"""
Problem Name : Best Time to Buy and Sell Stock
Category     : Sliding Window
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/sliding-window/SOLUTIONS.md#best-time-to-buy-and-sell-stock
NeetCode     : https://neetcode.io/problems/buy-and-sell-crypto
LeetCode     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP