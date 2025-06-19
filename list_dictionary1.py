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


odd_number={num for num in range (1,31) if num%2!=0}
set2=odd_number
print(set2)

#intersection
set3=set1.intersection(set2)
print(set3)

#union
set4=set1.union(set2)
print(set4)

#symmertric operation 
set5=set1.symmetric_difference(set2)
print(set5)