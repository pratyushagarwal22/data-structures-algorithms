"""
Problem Name : Valid Anagram
Category     : Arrays & Hashing
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/arrays-and-hashing/SOLUTIONS.md#valid-anagram
NeetCode     : https://neetcode.io/problems/is-anagram
LeetCode     : https://leetcode.com/problems/valid-anagram/description/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT