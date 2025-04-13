from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""1
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
48 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64""")

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
    for b in solutions:
        print(f"Board {counter}")
        counter+=1
        for r in b:
            print(r)
    