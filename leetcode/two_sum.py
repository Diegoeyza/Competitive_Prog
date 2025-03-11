class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Stores {num: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:  # Check if the complement exists in the dictionary
                return [num_map[complement], i]  # Return indices of the two numbers
            num_map[num] = i  # Store the current number with its index
        
        return []  # No solution found
