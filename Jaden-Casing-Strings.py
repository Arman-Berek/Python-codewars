# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
# Function capitalizes every word in string. 
def toJadenCase(string):
    s = ""
    for i in string.split():
        s += i.capitalize()
        s += " "
    s = s[:-1]
    return s