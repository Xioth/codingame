import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

sequence = [r]

for i in range(1, l):
    nextSequence = []
    number, last = 0, -1

    for element in sequence:
        if element != last:
            if number != 0:
                nextSequence.append(number)
                nextSequence.append(last)
            
            number = 1

        else:
            number += 1

        last = element

    nextSequence.append(number)
    nextSequence.append(last)
    sequence = nextSequence

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(' '.join(str(element) for element in sequence))
