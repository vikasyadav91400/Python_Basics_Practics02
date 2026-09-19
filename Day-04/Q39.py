#Find the sum of the digits of a number.
num = int(input("Enter a number: "))
sum_of_digits = 0
for i in str(num):
    sum_of_digits += int(i)
print("The sum of the digits of", num, "is:", sum_of_digits)