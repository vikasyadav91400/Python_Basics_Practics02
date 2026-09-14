#determin the type of triangle
def determine_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Right-angled triangle"
    else:
        return "Scalene triangle"
print(determine_triangle_type(3, 3, 5))    