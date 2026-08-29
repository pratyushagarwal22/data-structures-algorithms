"""
Problem Name : Valid Parentheses
Category     : Stack
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/stack/SOLUTIONS.md#valid-parentheses
NeetCode     : https://neetcode.io/problems/validate-parentheses/question?list=neetcode150
LeetCode     : https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0