from sys import stdin
import functools
import io


@functools.lru_cache(None)
def Hint(dolls,idx):
    current_max=1
    for j in range(idx+1, len(dolls)):
        if dolls[j][1]>=dolls[idx][1]: 
            current_max=max(current_max, 1 + Hint(dolls,j))
    return current_max 


# stdin = io.StringIO("""4
# 3
# 20 30 40 50 30 40
# 4
# 20 30 10 10 30 20 40 50
# 3
# 10 30 20 20 30 10
# 4
# 10 10 20 30 40 50 39 51""")

t=int(stdin.readline().strip())
for case in range(t):
    doll_c=int(stdin.readline().strip())
    line=list(map(int,stdin.readline().strip().split()))
    dolls=[]
    for i in range(len(line)//2):
        dolls.append((line[2*i],line[2*i+1]))
    # print(dolls)
    dolls.sort(key=lambda x:(-x[0],x[1]))
    resultado = 0

    for i in range(len(dolls)):
        resultado = max(resultado, Hint(tuple(dolls), i))
    print(resultado)