import re

def remove_vowels(s):
    return re.sub('[aeiou]', '', s)