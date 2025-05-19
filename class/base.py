from sys import stdin
import io
import math
import functools

@functools.lru_cache(None)   #improves recursive call speed
def something():
    return 0

stdin = io.StringIO("""12
10
5
0""")


input_value = int(stdin.readline().strip())

s, d = map(int, stdin.readline().split()) 
while s!="":
    try:
        s, d = map(int, stdin.readline().split()) 
    except:
        s=""