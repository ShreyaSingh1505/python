def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_set(n):
    primes = set()
    for num in range(2, n + 1):
        if is_prime(num):
            primes.add(num)
    return primes
n=30
set1=prime_numbers_set(n)
print(set1)


even_number={num for num in range (1,31) if num%2===0}
set2=even_number
print(set2)