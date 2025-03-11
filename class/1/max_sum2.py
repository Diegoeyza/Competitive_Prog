import io

stdin = io.StringIO("""4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2""")

lines = stdin.readlines()
size = int(lines[0])  
sq = [[int(x) for x in line.strip().split()] for line in lines[1:]]

max_sum = -10000 

for top in range(size):
    for left in range(size):
        for bottom in range(top, size):
            for right in range(left, size):
                val = 0
                for i in range(top, bottom + 1):
                    for j in range(left, right + 1):
                        val += sq[i][j]
                        print(sq[i][j])
                print("next")

                if val > max_sum:
                    max_sum = val

print(max_sum)