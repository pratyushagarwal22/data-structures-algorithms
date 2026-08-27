"""
Problem Name : Contains Duplicate
Category     : Arrays & Hashing
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/arrays-and-hashing/SOLUTIONS.md#contains-duplicate
NeetCode     : https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
LeetCode     : https://leetcode.com/problems/contains-duplicate/description/
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False