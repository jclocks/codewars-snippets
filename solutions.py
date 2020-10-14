###
#
# Codewars Solutions, by Johnny Tirado
#
###

# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e
# Returns a string with its vowels removed.
def disemvowel(string):
    for i in 'aeiouAEIOU':
        string = string.replace(i,'')
    return string

# Binary Addition
# https://www.codewars.com/kata/551f37452ff852b7bd000139
# Returns the sum of two numbers in binary, as a string.
def add_binary(a,b):
    return bin(a + b)[2:]

# Jaden Casing Strings
# https://www.codewars.com/kata/5390bac347d09b7da40006f6
# Takes string, returns same string but with the first letter of every word capitalized.
def to_jaden_case(string):
    words = string.split()
    for i in range(0,len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)

# Even or Odd
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# Takes number, returns "Even" or "Odd" depending on what it is.
def even_or_odd(number):
    if (number % 2) == 1:
        return "Odd"
    else:
        return "Even"

# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da
# Takes string, makes a string of numbers correlating to the position of the alphabet for each character, returns it.
import string
def alphabet_position(text):
    response = []
    for i in range(0,len(text)):
        if 1 <= int(ord(text[i].lower()) - 96) <= 26:
            response.append(str(ord(text[i].lower()) - 96))
    return ' '.join(response)

# More to come!
