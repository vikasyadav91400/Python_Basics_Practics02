
def is_palindrome(name):
    s = str(name)
    return s == s[::-1]


name = "vikas"
print(is_palindrome(name))