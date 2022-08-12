import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '?']

for i in range(h):
    row = input()
    result = ""

    for letter in t.lower():
        try:
            index = letters.index(letter)
        except:
            index = 26

        width = index * l
        result += row[width:width+l]
    
    print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
