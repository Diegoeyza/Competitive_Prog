def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0
    for i, num in enumerate(nums):
        if current_sum + num > num:
            current_sum += num  
        else:
            current_sum = num  
            temp_start = i 
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i
    return max_sum, [start, end]

def kadane_2D_cols(matrix, size):
    max_sum = float('-inf')
    final_top, final_bottom, final_left, final_right = 0, 0, 0, 0

    # Iterate over all possible column start points
    for left in range(size):
        kad = [0] * size  # Reset the row sum array when the col slider reaches the end
        
        # Expand the cols range (kinda like merging them)
        for right in range(left, size):
            for row in range(size):
                kad[row] += matrix[row][right]  # Compress row sums

            # Run Kadane on the row sum array
            max_local, (top, bottom) = kadane(kad)

            if max_local > max_sum:
                max_sum = max_local
                final_top, final_bottom = top, bottom
                final_left, final_right = left, right

    print(f"The max sum is {max_sum}, in the coordinates:")
    print(f"Top Left: ({final_top}, {final_left}), Bottom Right: ({final_bottom}, {final_right})")
    return max_sum, (final_top, final_left, final_bottom, final_right)

import io

stdin = io.StringIO("""4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2""")

lines = stdin.readlines()
size = int(lines[0])  
matrix = [[int(x) for x in line.strip().split()] for line in lines[1:]]

print(matrix)
kadane_2D_cols(matrix, size)
