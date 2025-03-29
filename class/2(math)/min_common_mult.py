from sys import stdin
import io
import math
stdin = io.StringIO("""12
10
5
9
0""")

case = 1  

input_value = int(stdin.readline().strip())

while input_value != 0:
    min_sum = float('inf')

    for i in range(1, int(math.sqrt(input_value)) + 1):
        if input_value % i == 0: 
            j = input_value // i  
            if i!=j:
                min_sum = min(min_sum, (i) + (j))

    if min_sum == float('inf'):
        min_sum = -1  

    print(f"Case {case}: {min_sum}")
    case += 1  
    input_value = int(stdin.readline().strip())