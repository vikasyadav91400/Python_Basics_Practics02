#calculate an elecricity bill using slabs.
units = int(input("Enter the number of units consumed: "))
if units <= 50:
    bill = units * 0.50
elif units <= 100:
    bill = 25 + (units - 50) * 0.75
elif units <= 200:
    bill = 62.50 + (units - 100) * 1.20
else:
    bill = 182.50 + (units - 200) * 1.50
print("The electricity bill is: Rs.", bill)