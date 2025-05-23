from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""9 
1 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 0 0 0 0 1 0 0 
0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 1 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
78 53 31 36 98 52 79 36 
2 91 87 53 68 18 96 41 
44 43 71 48 94 46 17 56 
4 35 27 39 61 80 43 9 
49 56 95 3 33 16 45 54 
82 16 96 12 43 50 83 59 
48 79 21 66 29 19 89 72 
85 98 81 97 91 14 71 82 
3 27 94 76 98 96 68 55 
99 26 86 91 24 92 32 66 
35 51 60 34 18 77 59 31 
11 36 83 59 33 52 40 99 
8 55 16 29 74 96 64 56 
63 78 85 61 78 23 63 94 
69 10 82 45 51 4 72 97 
28 19 10 62 25 6 45 88 
28 57 60 77 66 83 14 69 
63 56 33 38 15 91 56 66 
4 31 92 40 56 57 34 33 
74 40 58 96 36 62 53 68 
2 67 33 85 20 3 52 10 
75 67 76 85 73 22 49 6 
67 14 1 8 95 63 15 96 
64 16 28 3 76 83 77 65 
56 45 53 62 12 65 75 78 
61 37 70 11 26 9 43 29 
83 75 30 78 61 24 39 42 
1 81 32 59 87 98 97 89 
3 70 44 67 54 59 40 83 
65 10 81 74 81 19 94 53 
55 60 13 37 84 9 90 24 
71 98 90 96 43 9 53 60 
38 47 43 2 92 43 59 24 
17 61 89 77 82 91 23 91 
67 29 87 6 30 65 18 91 
47 50 36 95 52 88 41 88 
39 97 97 21 12 45 12 96 
27 79 75 71 6 35 3 53 
93 65 5 65 93 10 22 87 
85 34 6 76 62 85 17 78 
73 68 61 19 25 67 27 97 
94 79 35 51 63 33 71 44 
92 80 23 34 10 24 68 59 
24 76 49 10 47 19 96 39 
89 28 96 45 79 84 4 19 
3 97 72 62 2 40 26 66 
99 98 11 80 43 75 77 46 
85 28 27 17 27 75 57 67 
0 0 0 0 0 10 0 0 
0 10 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 10 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
12 56 12 98 36 1 4 9 
23 98 2 5 47 8 17 94 
8 2 3 6 8 4 76 3 
46 7 45 43 6 67 23 54 
8 65 4 2 46 2 7 46 
24 45 67 87 4 2 76 8 
3 3 6 8 7 4 3 6 
94 2 2 76 67 43 4 42 
""")

def set_queens(used_cols,used_pos_diags,used_neg_diags,current_row,positions,solutions):
    if current_row==8:
        solutions.append([row[:] for row in positions])
        return
    
    
    for i in range (8):
        pos_diag=calculate_pos_diagonal(current_row,i)
        neg_diag=calculate_neg_diagonal(current_row,i)
        if (i in used_cols or pos_diag in used_pos_diags or neg_diag in used_neg_diags):
            continue

        used_cols.add(i)
        used_neg_diags.add(neg_diag)
        used_pos_diags.add(pos_diag)
        positions[current_row][i]=1
        set_queens(used_cols,used_pos_diags,used_neg_diags,current_row+1,positions,solutions)

        positions[current_row][i] = 0
        used_cols.remove(i)
        used_pos_diags.remove(pos_diag)
        used_neg_diags.remove(neg_diag)




def calculate_pos_diagonal(row,col): #calculates the diagonal that goes to the upper right
    return row+col
def calculate_neg_diagonal(row,col):
    return row-col

def calculate_board_scores(board,solutions):
    score=[]
    for solution in solutions:
        sol_score=0
        for row in range (len(solution)):
            for col in range(len(solution[row])):
                if solution[row][col]==1:
                    sol_score+=board[row][col]
        score.append(sol_score)
    return score



    


boards = int(stdin.readline().strip())
for i in range (boards):
    board=[[0 for i in range (8)] for j in range (8)]
    for j in range (8):
        board[j]= [int(i) for i in stdin.readline().split()]
    used_cols=set()
    used_pos_diags=set()
    used_neg_diags=set()
    positions = [[0 for _ in range(8)] for _ in range(8)]
    solutions = []
    set_queens(used_cols,used_pos_diags,used_neg_diags,0,positions,solutions)
    counter=1
    # for b in solutions:
    #     print(f"Board {counter}")
    #     counter+=1
    #     for r in b:
    #         print(r)

    val=str(max(calculate_board_scores(board,solutions)))
    print(" "*(5-len(val))+val)
    