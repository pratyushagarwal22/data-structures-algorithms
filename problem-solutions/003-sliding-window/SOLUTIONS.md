# Sliding Window

Maintaining a moving contiguous range to track subarray/substring properties efficiently.

[← Back to README](../../README.md)

---

Problems will be added below as they are solved. Copy from [PROBLEM_TEMPLATE.md](../../templates/PROBLEM_TEMPLATE.md) for each new entry.

---

<!-- PROBLEMS START HERE -->

---

## Best Time to Buy and Sell Stock

🔗 [NeetCode](https://neetcode.io/problems/buy-and-sell-crypto) | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) | 🟢 Easy | 📁 [121_best_time_to_buy_and_sell_stock.py](./121_best_time_to_buy_and_sell_stock.py)

### Problem Statement
Given an array of daily stock prices, find the maximum profit possible by buying on one day and selling on a future day. Return 0 if no profitable transaction exists.

### Approach

- **Pattern:** Sliding Window (Two Pointers)
- **Why it fits:** We maintain a window where left is the buy day and right is the sell day, always moving forward in time. We never need to look back — if we find a lower price, that becomes our new buy point.
- **Key Insight:** Treat every price as a potential sell point. The best buy point for any sell day is always the minimum price seen so far to its left. If the current price is lower than our buy pointer, it's a better buy — shift left to it.
- **Algorithm Strategy:**
  1. Initialize left at index 0 (buy), right at index 1 (sell), maxProfit at 0
  2. While right is within bounds, check if prices[left] < prices[right]
  3. If yes, calculate profit and update maxProfit
  4. If no, the right pointer found a lower price — move left to right
  5. Always advance right by 1
  6. Return maxProfit

### Pseudocode

```
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
```

### Complexity

- **Time:** O(n) — single pass through the array
- **Space:** O(1) — only tracking two pointers and a max value

### Notes & Gotchas

- You must buy before you sell — left always stays behind right since we only move left forward when right finds a cheaper price
- If prices are strictly decreasing, left and right end up adjacent at every step and maxProfit stays 0 — correct behavior
- Brute force nested loop is O(n²) — not acceptable at scale
