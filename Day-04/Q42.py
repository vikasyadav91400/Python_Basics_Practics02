# Check whether a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(2))  # True
print(is_prime(17))  # True
print(is_prime(4))  # False