import random
numbers = [random.randint(100, 900) for _ in range(100)]
odd = []
even = []
prime = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
print("All Odd Numbers:", odd)
print("Count of Odd Numbers:", len(odd))
print("\nAll Even Numbers:", even)
print("Count of Even Numbers:", len(even))
print("\nAll Prime Numbers:", prime)
print("Count of Prime Numbers:", len(prime))