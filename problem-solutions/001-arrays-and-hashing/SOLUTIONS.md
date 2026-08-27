# Arrays & Hashing

Using arrays and hash maps/sets for O(1) lookups, frequency counting, and deduplication.

[← Back to README](../../README.md)

---

Problems will be added below as they are solved. Copy from [PROBLEM_TEMPLATE.md](../../templates/PROBLEM_TEMPLATE.md) for each new entry.

---

<!-- PROBLEMS START HERE -->
---

## 217 - Contains Duplicate

🔗 [NeetCode](https://neetcode.io/problems/duplicate-integer/question?list=neetcode150) | [LeetCode](https://leetcode.com/problems/contains-duplicate/description/) | 🟢 Easy | 📁 [217_contains_duplicate.py](./217_contains_duplicate.py)

### Problem Statement
Given an integer array, return true if any value appears more than once, otherwise return false.

### Approach

- **Pattern:** Hash Set
- **Why it fits:** We need O(1) membership checks as we scan through the array — a set gives us exactly that, letting us detect a duplicate the moment we see it again.
- **Key Insight:** Instead of comparing every element against every other element (O(n²)), store each number in a set as you go. If you ever try to add a number that's already there, you've found your duplicate.
- **Algorithm Strategy:**
  1. Initialize an empty set
  2. Iterate through each number in the array
  3. If the number is already in the set, return True
  4. Otherwise add it to the set and continue
  5. If the loop finishes with no duplicate found, return False

### Pseudocode

```
seen = empty set
for num in nums:
    if num in seen:
        return True
    add num to seen
return False
```

### Complexity

- **Time:** O(n) — single pass through the array; each set lookup and insert is O(1)
- **Space:** O(n) — worst case (no duplicates) we store every element in the set

### Notes & Gotchas

- Empty array: loop never runs, returns False — correct behavior
- Don't confuse `set` with `dict` — we only need membership, not key-value pairs
- Beats sorting O(n log n) and nested loops O(n²)