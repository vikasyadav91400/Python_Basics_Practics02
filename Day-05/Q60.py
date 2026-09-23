# Check whether two strings are anagrams.
def is_anagram(str1, str2 ):
    s1=str1.replace(" ", "").lower()
    s2=str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
print(is_anagram("Listen", "Silent"))
print(is_anagram("Vikas", "Akash"))