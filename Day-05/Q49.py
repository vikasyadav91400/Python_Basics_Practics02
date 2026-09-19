#count vowels in string
name="vikas"
vowels="aeiou"
count=0
for i in name:
    if i in vowels:
        count+=1
print(count)