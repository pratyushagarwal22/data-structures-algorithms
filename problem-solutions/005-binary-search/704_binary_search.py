"""
Problem Name : Binary Search
Category     : Binary Search
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/binary-search/SOLUTIONS.md#binary-search
NeetCode     : https://neetcode.io/problems/binary-search
LeetCode     : https://leetcode.com/problems/binary-search/description/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1