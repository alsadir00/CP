# 976. Largest Perimeter Triangle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_array = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sorted_array[i] != heights[i]:
                count += 1
        return count
