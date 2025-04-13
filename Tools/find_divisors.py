def find_divisors(n):
    divisors = set()
    for d in range(1, int(abs(n) ** 0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(-d)
            divisors.add(n // d)
            divisors.add(-n // d)
    return divisors

print(find_divisors(456))