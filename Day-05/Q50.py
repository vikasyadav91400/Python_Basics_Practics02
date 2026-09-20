#count consonants in a string
def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count    

# Example usage
text = "Hello, World!"
print(count_consonants(text))  
