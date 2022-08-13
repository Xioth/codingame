import sys
import math
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
binary = (' '.join(format(ord(character), '#09b') for character in message)).replace(' ', '').replace('0b', '')
bitGroup = [''.join(bit) for _, bit in itertools.groupby(binary)]
result = ''

for bits in bitGroup:
    if '1' in bits:
        result += '0'
    elif '0' in bits:
        result += '00'

    result += ' ' + bits.replace('1', '0') + ' '

result = result[:-1]
print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
