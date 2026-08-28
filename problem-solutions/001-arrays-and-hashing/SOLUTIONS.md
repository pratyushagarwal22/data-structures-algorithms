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

---

## Two Sum

🔗 [NeetCode](https://neetcode.io/problems/two-integer-sum) | [LeetCode](https://leetcode.com/problems/two-sum/description/) | 🟢 Easy | 📁 [002_two_sum.py](./002_two_sum.py)

### Problem Statement
Given an array of integers and a target value, return the indices of the two numbers that add up to the target. The smaller index should come first. Exactly one valid answer is guaranteed.

### Approach

- **Pattern:** Hash Map
- **Why it fits:** We need to find a complement for each number in O(1) — a hash map lets us store numbers we've already seen and look up their index instantly.
- **Key Insight:** For every number, the answer is already determined — it's `target - num`. So instead of searching the array for that complement, just check if it's already in the map as you go.
- **Algorithm Strategy:**
  1. Initialize an empty hash map (num → index)
  2. Iterate through the array
  3. Calculate complement = target - current number
  4. If complement is in the map, return [map[complement], current index]
  5. Otherwise store current number and its index in the map

### Pseudocode

```
hashmap = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
        return [hashmap[complement], i]
    hashmap[num] = i
```

### Complexity

- **Time:** O(n) — single pass through the array; each hash map lookup and insert is O(1)
- **Space:** O(n) — worst case we store every element in the hash map before finding the answer

### Notes & Gotchas

- Return the smaller index first — since we iterate left to right, `hashmap[complement]` is always the earlier index
- The problem guarantees exactly one answer so no need to handle the no-result case
- Brute force nested loop approach works but is O(n²) — not acceptable at scale

---

## Valid Anagram

🔗 [NeetCode](https://neetcode.io/problems/is-anagram) | [LeetCode](https://leetcode.com/problems/valid-anagram/description/) | 🟢 Easy | 📁 [242_valid_anagram.py](./242_valid_anagram.py)

### Problem Statement
Given two strings, return true if they are anagrams of each other — meaning they contain the exact same characters with the same frequency, regardless of order.

### Approach

- **Pattern:** Hash Map (Character Frequency Count)
- **Why it fits:** An anagram is just a frequency equality problem. A hash map lets us count occurrences of each character in O(n) and compare both maps directly.
- **Key Insight:** Two strings are anagrams if and only if their character frequency maps are identical. Length check first as an early exit — if lengths differ they can't be anagrams.
- **Algorithm Strategy:**
  1. If lengths differ, return False immediately
  2. Build a frequency map for each string simultaneously in one loop
  3. Return whether the two maps are equal

### Pseudocode

```
if len(s) != len(t):
    return False

countS, countT = {}, {}
for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)

return countS == countT
```

### Complexity

- **Time:** O(n + m) — one pass to build both frequency maps, where n and m are the lengths of s and t
- **Space:** O(1) — at most 26 keys in each map since input is lowercase English letters only

### Notes & Gotchas

- Space is technically O(1) not O(n) here because the character set is fixed at 26 letters
- Sorting approach (O(n log n)) is simpler to write but less optimal
- `dict.get(key, 0)` is the clean way to handle missing keys without a try/except or if/else