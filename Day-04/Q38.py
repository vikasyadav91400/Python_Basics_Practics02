#count a digit in a number
num = int(input("Enter a number: "))
digit = int(input("Enter the digit to count: "))
count = 0
for i in str(num):
    if i == str(digit):
        count += 1
print("The digit", digit, "appears", count, "times in the number", num)