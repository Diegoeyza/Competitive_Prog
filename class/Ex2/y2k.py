from sys import stdin
import io

def backtraking(curr_months,s,d):
    if len(curr_months)==12:
        total=0
        for val in curr_months:
            total+=val
        if total>0:
            return True
        else:
            return False
    if len(curr_months)>4:
        check=curr_months[-5:]
        profit=0
        for val in check:
            profit+=val
        if profit>=0:
            return False
    
    curr_months.append(-d)
    if backtraking(curr_months,s,d)>0:
        return True
    curr_months.pop()
    curr_months.append(s)
    if backtraking(curr_months,s,d)>0:
        return True
    curr_months.pop()
    return False
    
# stdin = io.StringIO("""59 237
# 375 743
# 200000 849694
# 2500000 8000000
# """)
    
        
s, d = map(int, stdin.readline().split()) 
while s!="":
    months=[]
    if backtraking(months,s,d):
        print(sum(months))
    else:
        print("Deficit")
    try:
        s, d = map(int, stdin.readline().split()) 
    except:
        s=""