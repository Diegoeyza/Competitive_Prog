from sys import stdin
import io
import math

def calculate_digs(power_2):
    c = power_2 * math.log10(2)
    digits = int(c) + 1
    first_d = 10 ** (c % 1) 
    return [digits, int(first_d * 10**(len(str(n)) - 1))] 

def powers(n):
    power_2 = 1
    while True:  
        d_count, first_d = calculate_digs(power_2)
        
        if len(str(n)) * 2 < d_count and str(n) == str(first_d)[:len(str(n))]:
            return power_2 
        
        power_2 += 1 

stdin = io.StringIO("""1
2
10""")

while True:
    try:
        n = int(stdin.readline().strip())
        if n == 0:
            break
        print(f"input= {n}")
        print(powers(n))
    except:
        break
