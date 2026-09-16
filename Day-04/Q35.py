#find the sum from 1 to N
N = int(input("Enter the value of N: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print("The sum from 1 to", N, "is:", sum)