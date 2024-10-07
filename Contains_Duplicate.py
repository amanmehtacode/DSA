# Duplicate Integer

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to track seen numbers
        hashset = set()
        
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, we have a duplicate
            if num in hashset:
                return True
            else:
                # Otherwise, add the number to the set
                hashset.add(num)
        
        # If no duplicates are found, return False
        return False
    
    # Time Complexity:
    # O(n) - We iterate through each number in the list once
    # Space Complexity:
    # O(n) - We store at most n numbers in the set
    # where n is the length of the input list
    