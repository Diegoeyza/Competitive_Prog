def fib_rec(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return fib_rec(n-1)+fib_rec(n-2)

mem_rec={
    0:0,
    1:1
}

def fib_rec_mem(n):
    if n not in mem_rec:
        mem_rec[n]=fib_rec_mem(n-1)+fib_rec_mem(n-2)
    return mem_rec[n]

print(fib_rec_mem(8))

##forma bonita de aplicar memoria

class Memorize:
    def __init__(self,f):
        self.f=f
        self.memo={}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args]=self.f(*args)
        return self.memo[args]