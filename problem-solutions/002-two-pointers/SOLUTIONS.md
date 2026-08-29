# Two Pointers

Coordinating two indices moving through a sequence to shrink the search space in linear time.

[← Back to README](../../README.md)

---

Problems will be added below as they are solved. Copy from [PROBLEM_TEMPLATE.md](../../templates/PROBLEM_TEMPLATE.md) for each new entry.

---

<!-- PROBLEMS START HERE -->

---

## Valid Palindrome

🔗 [NeetCode](https://neetcode.io/problems/is-palindrome) | [LeetCode](https://leetcode.com/problems/valid-palindrome/description/) | 🟢 Easy | 📁 [125_valid_palindrome.py](./125_valid_palindrome.py)

### Problem Statement
Given a string, return true if it is a palindrome after removing all non-alphanumeric characters and ignoring case. A palindrome reads the same forward and backward.

### Approach

- **Pattern:** Two Pointers
- **Why it fits:** We need to compare characters from both ends moving inward — two pointers let us do this in O(n) with O(1) space, no copy needed.
- **Key Insight:** Strip and lowercase the string first to isolate only the characters that matter, then use two pointers converging from both ends. If they ever disagree, it's not a palindrome.
- **Algorithm Strategy:**
  1. Build a cleaned string keeping only alphanumeric characters, lowercased
  2. Initialize left pointer at start, right pointer at end
  3. While left < right, compare characters at both pointers
  4. If they don't match, return False
  5. Otherwise move both pointers inward and continue
  6. If the loop completes, return True

### Pseudocode

```
cleaned = ""
for c in s:
    if c.isalnum():
        cleaned += c.lower()

L, R = 0, len(cleaned) - 1
while L < R:
    if cleaned[L] != cleaned[R]:
        return False
    L += 1
    R -= 1
return True
```

### Complexity

- **Time:** O(n) — one pass to clean the string, one pass for the two pointer comparison
- **Space:** O(n) — the cleaned string stores up to n characters

### Notes & Gotchas

- `isalnum()` handles both letters and digits in one check — no need to check separately
- The truly O(1) space solution skips building the cleaned string entirely and handles non-alphanumeric characters by advancing the pointer — worth knowing for follow-up questions
- Empty string and single character inputs are valid palindromes — the while loop handles both correctly