import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)
