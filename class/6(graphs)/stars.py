import sys
import io


sys.stdin = io.StringIO("""5 5
.....
....*
....*
...*.
*....
4 3
...
.*.
...
*.*
0 0
""")



def is_valid(r, c, i, j):
    if (0 <= i < r and 0 <= j < c):
        return True
    return False

def dfs(grid, visited, r, c, i, j):
    visited[i][j] = True
    neighbors = []
    for dx, dy in directions:
        ni=i+dx
        nj=j+dy
        if is_valid(r, c, ni, nj) and not visited[ni][nj] and grid[ni][nj] == '*':
            neighbors.append((ni, nj))
            dfs(grid, visited, r, c, ni, nj)
    return neighbors

directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0), (1, 1)]
while True:
    line = sys.stdin.readline()
    if not line:
        break
    r, c = map(int, line.strip().split())
    # print(r)
    if r == 0 and c == 0:
        break
    grid = [list(sys.stdin.readline().strip()) for i in range(r)]
    visited = [[False] * c for i in range(r)]
    star_count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '*' and not visited[i][j]:
                neighbors = dfs(grid, visited, r, c, i, j)
                if not neighbors:
                    star_count += 1

    print(star_count)
