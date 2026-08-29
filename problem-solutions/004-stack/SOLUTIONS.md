# Stack

Leveraging LIFO ordering to process nested structures, monotonic sequences, and expression parsing.

[← Back to README](../../README.md)

---

Problems will be added below as they are solved. Copy from [PROBLEM_TEMPLATE.md](../../templates/PROBLEM_TEMPLATE.md) for each new entry.

---

<!-- PROBLEMS START HERE -->

---

## Valid Parentheses

🔗 [NeetCode](https://neetcode.io/problems/validate-parentheses/question?list=neetcode150) | [LeetCode](https://leetcode.com/problems/valid-parentheses/description/) | 🟢 Easy | 📁 [020_valid_parentheses.py](./020_valid_parentheses.py)

### Problem Statement
Given a string containing only brackets — `()`, `{}`, `[]` — return true if every opening bracket is closed by the correct type of bracket in the correct order.

### Approach

- **Pattern:** Stack
- **Why it fits:** Brackets have a last-in-first-out relationship — the most recently opened bracket must be the next one closed. A stack naturally models this nesting behavior.
- **Key Insight:** Map every closing bracket to its expected opening bracket. As you scan left to right, push opening brackets onto the stack. When you hit a closing bracket, check if it matches the top of the stack — if not, the string is invalid. If the stack is empty at the end, every bracket was matched correctly.
- **Algorithm Strategy:**
  1. Build a map of closing → opening brackets
  2. Initialize an empty stack
  3. For each character in the string:
     - If it's a closing bracket, check if the top of the stack is its matching opener
     - If yes, pop the stack; if no (or stack is empty), return False
     - If it's an opening bracket, push it onto the stack
  4. Return True only if the stack is empty

### Other Approaches

- **Brute Force (String Replacement):** Repeatedly replace valid pairs `()`, `{}`, `[]` with empty string until no more replacements can be made. If the string is empty, return True. O(n²) time — each replacement pass is O(n) and there can be O(n) passes.
- **Counter-based (only works for single bracket type):** Track open count with a counter, increment on `(`, decrement on `)`, return False if counter goes negative. Breaks down with mixed bracket types like `([)]` so not applicable here.

### Pseudocode

```
closeToOpen = { ")": "(", "}": "{", "]": "[" }
stack = []

for c in s:
    if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
        else:
            return False
    else:
        stack.append(c)

return len(stack) == 0
```

### Complexity

- **Time:** O(n) — single pass through the string, each push and pop is O(1)
- **Space:** O(n) — worst case the stack holds all characters e.g. `(((((`

### Notes & Gotchas

- Always check `if stack` before accessing `stack[-1]` — popping an empty stack will throw an error
- `[(])` is invalid even though bracket counts match — order matters, which is exactly why a counter-based approach fails here
- `return len(stack) == 0` is cleaner than an if/else — worth simplifying in an interview
