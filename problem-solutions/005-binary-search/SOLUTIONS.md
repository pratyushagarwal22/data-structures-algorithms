# Binary Search

Halving a sorted or monotonic search space to find answers in logarithmic time.

[← Back to README](../../README.md)

---

Problems will be added below as they are solved. Copy from [PROBLEM_TEMPLATE.md](../../templates/PROBLEM_TEMPLATE.md) for each new entry.

---

<!-- PROBLEMS START HERE -->

---

## Binary Search

🔗 [NeetCode](https://neetcode.io/problems/binary-search) | [LeetCode](https://leetcode.com/problems/binary-search/description/) | 🟢 Easy | 📁 [704_binary_search.py](./704_binary_search.py)

### Problem Statement
Given a sorted array of distinct integers and a target value, return the index of the target if it exists, otherwise return -1. Must run in O(log n) time.

### Approach

- **Pattern:** Binary Search
- **Why it fits:** The array is sorted, which means at any midpoint we can eliminate half the search space — the core property that makes binary search applicable.
- **Key Insight:** At each step, compare the middle element to the target. If it's too big, the answer must be in the left half. If it's too small, it must be in the right half. Repeat until found or the search space is empty.
- **Algorithm Strategy:**
  1. Initialize left at 0, right at len(nums) - 1
  2. While left <= right, calculate mid = (left + right) // 2
  3. If nums[mid] > target, move right to mid - 1
  4. If nums[mid] < target, move left to mid + 1
  5. If nums[mid] == target, return mid
  6. If the loop exits without returning, return -1

### Pseudocode

```
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] > target:
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        return mid

return -1
```

### Complexity

- **Time:** O(log n) — search space halves on every iteration
- **Space:** O(1) — only tracking two pointers and a midpoint

### Notes & Gotchas

- Use `mid = left + (right - left) // 2` in languages prone to integer overflow (Java, C++) — not a concern in Python but good habit for interviews
- The condition is `left <= right` not `left < right` — without the `=` you miss the case where the target is the last remaining element
- Only works on sorted input — always confirm this assumption in an interview
