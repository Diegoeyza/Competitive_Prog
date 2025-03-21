from sys import stdin
import io

def f91(n):
    if n > 100:
        return n - 10
    return f91(f91(n + 11))
    


input = int(stdin.readline())
while (input != 0):
    print(f"f91({input}) = {f91(input)}")
    input=int(stdin.readline())