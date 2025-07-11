#Problem link 
 https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

#Problem Summary
Given an array, determine if it was originally sorted in non-decreasing order, then rotated.

class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0  # Initialize counter to count how many times the order breaks
        
        # Loop through all elements in the array
        for i in range(len(nums)):
            # Compare current element with the next one (circular using %)
            if nums[i] > nums[(i + 1) % len(nums)]:
                counter += 1  # If current > next, it's a "drop", so increment counter
        
        # If there's more than one "drop", it's not a rotated sorted array
        if counter > 1:
            return False
        else:
            return True
