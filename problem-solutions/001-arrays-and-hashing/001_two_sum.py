"""
Problem Name : Two Sum
Category     : Arrays & Hashing
Difficulty   : EASY
Write-up     : https://github.com/pratyushagarwal22/data-structures-algorithms/blob/main/problem-solutions/arrays-and-hashing/SOLUTIONS.md#two-sum
NeetCode     : https://neetcode.io/problems/two-integer-sum
LeetCode     : https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []