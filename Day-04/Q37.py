#find the factorial of N
n = int(input("Enter the value of N: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is:", factorial)