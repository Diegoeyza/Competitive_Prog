# def el(n):
#     return n**2

# l=[1,2,3,4]


# for item in filter(lambda x: x<2,l):
#     print(item)

# def extend_solution(assignment, n):
#     workers = sorted([w for (w,t) in assignment])
#     tasks = sorted([t for (w,t) in assignment])
#     free_workers = [x for x in range(n) if x not in workers]
#     free_tasks = [x for x in range(n) if x not in tasks]

#     print("Current assignment:", assignment)
#     print("Assigned workers:", workers)
#     print("Assigned tasks:", tasks)
#     print("Free workers:", free_workers)
#     print("Free tasks:", free_tasks)

#     for t in free_workers:
#         for T in free_tasks:
#             new_assignment = assignment + [(t, T)]
#             print(f"Yielding: {new_assignment}")
#             yield new_assignment

# list(extend_solution([(0, 1)], 3))

a="hello"
print(a[:-1])