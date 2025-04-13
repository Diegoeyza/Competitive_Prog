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

def set_queens(board):
    positions=[[0]*8]*8

def calculate_pos_diagonal(row,col): #calculates the diagonal that goes to the upper right
    return row+col
def calculate_neg_diagonal(row,col):
    return row-col


    


boards = int(stdin.readline().strip())
for i in range (boards):
    board=[[0]*8]*8
    for j in range (8):
        board[j]= [int(i) for i in stdin.readline().split()]
    set_queens(board)
    