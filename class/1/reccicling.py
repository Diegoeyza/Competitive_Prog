import io

stdin = io.StringIO("""1 2 3 4 5 6 7 8 9""")
'''Brown, Green, Clear'''
lines = stdin.readlines()

matrix = [[int(x) for x in line.strip("\n").split(" ")] for line in lines][0]
print(matrix)
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
        print(start)
        print(f"{elements[start]}, {elements[i]}")
        generate_permutations(elements, start + 1, orders)
        # Swap back to restore the original order (backtracking)
        elements[start], elements[i] = elements[i], elements[start]

orders = []
current = ["B", "G", "C"]
generate_permutations(current, 0, orders)

# Print all unique orders
for order in orders:
    print(order)

'''
for i in range (3):
    for j,item in enumerate(matrix):
'''
