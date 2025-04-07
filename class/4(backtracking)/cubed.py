from sys import stdin
import io

stdin = io.StringIO("""4
123
1234567
435621
9876543213""")

def construct(n):
    result=0
    for position in range(len(str(n))):
        mod = 10**(position+1)
        for digit in range(10):
            res = result+digit*(10**position)
            if res!=0:
                if (res**3)%mod==n%mod:
                    result=res
                    break
    return result




cases = int(stdin.readline())
for j in range(cases):
    num = int(stdin.readline())
    # find(num)
    l=[]
    print(construct(num))

