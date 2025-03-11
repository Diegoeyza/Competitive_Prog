def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i, num in enumerate(nums):
        if current_sum + num > num:
            current_sum += num  # Extend the subarray
        else:
            current_sum = num  # Start new subarray
            temp_start = i  # New potential start

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i  # Update best subarray indices

    return max_sum, nums[start:end+1]

# Example test cases
nums1 = [3, -2, -7, 4, 5, -6, 7, -100, 10, 0, 9, -5, 9, 10, 8, -5, 8, -4, 7]
nums2 = [-1, -2, -3, -4, -5]  # All-negative case
nums3 = [5, -2, 3, 4, -1, 2, 1, -5, 4]  # Typical mixed case

print(kadane(nums1))  # (47, [10, 0, 9, -5, 9, 10, 8, -5, 8, -4, 7])
print(kadane(nums2))  # (-1, [-1])
print(kadane(nums3))  # (12, [5, -2, 3, 4, -1, 2, 1])
