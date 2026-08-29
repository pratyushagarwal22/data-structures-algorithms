"""
Problem Name : Valid Palindrome
Category     : Two Pointers
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/two-pointers/SOLUTIONS.md#valid-palindrome
NeetCode     : https://neetcode.io/problems/is-palindrome
LeetCode     : https://leetcode.com/problems/valid-palindrome/description/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        L, R = 0, len(newStr) - 1

        while L < R:
            if newStr[L] != newStr[R]:
                return False
            L += 1
            R -= 1
        return True