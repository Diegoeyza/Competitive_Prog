from sys import stdin
import io
import math
import time
stdin = io.StringIO("""13
2""")

def find_primes(limit, starter):
    prime = bytearray([True]) * (limit + 1)
    prime[0]=False
    prime[1]=False

    for num in range(2, int(math.sqrt(limit)) + 1):
        if prime[num]:
            prime[num*num:limit+1:num] = bytearray([False]) * len(range(num*num, limit+1, num))
    return [i for i in range(starter + 1, limit + 1) if prime[i]]

def find_candidates(primes,num_sum):
    candidates = set()
    for num in primes:
        if sum(map(int, str(num))) == num_sum:
            candidates.add(num)
    return candidates

def find_first(primes,first):
    first_cand=set()
    for num in primes:
        if num//10000==int(first):
            first_cand.add(num)
    return first_cand

def construct(primes, first):
    prime_set = set(primes)
    first_cand = list(find_first(primes, first))
    candidates = [list(map(int, str(p))) for p in primes]

    col_prefixes = [set() for i in range(6)]
    diag_prefixes = [set() for i in range(6)]
    anti_diag_prefixes = [set() for i in range(6)]

    for num in primes:
        s = str(num)
        for l in range(1, 6):
            prefix = int(s[:l])
            for i in range(5):
                col_prefixes[l].add(int("".join(s[:l])))
            diag_prefixes[l].add(int("".join(s[:l])))
            anti_diag_prefixes[l].add(int("".join(s[:l])))

    solutions = []

    def get_col(board, col, upto):
        return int("".join(str(board[i][col]) for i in range(upto)))
    def get_diag(board, upto):
        return int("".join(str(board[i][i]) for i in range(upto)))
    def get_anti_diag(board, upto):
        return int("".join(str(board[i][4 - i]) for i in range(upto)))



    #probando verificar antes de que se terminen de agregar todas las filas
    def part_val(board, row_idx):
        for col in range(5):
            col_val = get_col(board, col, row_idx + 1)
            if col_val not in col_prefixes[row_idx + 1]:
                return False
        if get_diag(board, row_idx + 1) not in diag_prefixes[row_idx + 1]:
            return False
        if get_anti_diag(board, row_idx + 1) not in anti_diag_prefixes[row_idx + 1]:
            return False
        return True




    def is_full_valid(board):
        for col in range(5):
            num = int("".join(str(board[row][col]) for row in range(5)))
            if num not in prime_set:
                return False
        diag = int("".join(str(board[i][i]) for i in range(5)))
        anti_diag = int("".join(str(board[i][4 - i]) for i in range(5)))
        return diag in prime_set and anti_diag in prime_set

    def backtrack(row_idx, board):
        if row_idx == 5:
            if is_full_valid(board):
                solutions.append([row[:] for row in board])
            return

        for row_digits in candidates:
            board[row_idx] = row_digits
            if part_val(board, row_idx):
                backtrack(row_idx + 1, board)

    for prime in first_cand:
        board = [[0]*5 for k in range(5)]
        board[0] = [int(d) for d in str(prime)]
        backtrack(1, board)

    return solutions



start=time.time()
total_sum = int(stdin.readline().strip())
d=int(stdin.readline().strip())
primes=find_primes(99999,10000)
candidates=find_candidates(primes,total_sum)
sol=sorted(construct(candidates,d))
x=1
for item in sol:
    # print(f"Solution {x}")
    # x+=1
    for row in item:
        print("".join(str(row[i]) for i in range (len(row))))
    print("\n")
end=time.time()
print(f"exec time={end-start}")

