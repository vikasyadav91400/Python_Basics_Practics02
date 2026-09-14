# arrange three numbers in ascending order
def arrange_numbers(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            return a, b, c
        else:
            return a, c, b
    elif b <= a and b <= c:
        if a <= c:
            return b, a, c
        else:
            return b, c, a
    else:
        if a <= b:
            return c, a, b
        else:
            return c, b, a
        
print(arrange_numbers(3, 1, 2))
