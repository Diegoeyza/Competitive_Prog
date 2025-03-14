import io

stdin = io.StringIO("""1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10""")
'''Brown, Green, Clear'''
lines = stdin.readlines()

matrix = [[int(x) for x in line.strip("\n").split(" ")] for line in lines]
movements=[]
count=1
pos=0
def generate_permutations(elements, start=0, orders=[]):
    if start == len(elements) - 1:
        orders.append(elements[:])  # Store a copy of the current permutation
        return
    
    for i in range(start, len(elements)):
        # Swap elements to create a new order
        elements[start], elements[i] = elements[i], elements[start]
        generate_permutations(elements, start + 1, orders)
        # Swap back to restore the original order (backtracking)
        elements[start], elements[i] = elements[i], elements[start]

orders = []
current = ["B", "G", "C"]
generate_permutations(current, 0, orders)

for li in matrix:
    total_movements=[0]*len(orders)

    for i in range (len(orders)):
        for j,item in enumerate(li):
            if (j<3):
                idx=orders[i].index("B")
                if (idx!=j):
                    total_movements[i]+=li[j]
            elif (j<6):
                idx=orders[i].index("G")
                if (idx!=j-3):
                    total_movements[i]+=li[j]
                pass
            else:
                idx=orders[i].index("C")
                if (idx!=j-6):
                    total_movements[i]+=li[j]
                pass
    result=min(total_movements)
    best=orders[total_movements.index(result)]
    print(f"{''.join(best)} {result}")