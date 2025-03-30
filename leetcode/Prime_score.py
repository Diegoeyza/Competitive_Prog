def prime_score(n):
    distinct_primes = set()
    i = 2

    while i * i <= n:
        while n % i == 0:
            distinct_primes.add(i)
            n //= i
        i += 1
    
    if n > 1:
        distinct_primes.add(n)  # If n is prime itself

    return len(distinct_primes)


print(prime_score(300))