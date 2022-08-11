import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
values = []
gap = []

for i in range(n):
    pi = int(input())
    values.append(pi)

values.sort()

for i in range(len(values) - 1):
    gap.append(abs(values[i] - values[i+1]))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

result = min(gap)
print(result)
