import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext_dict = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_dict[ext.lower()] = mt

for i in range(q):
    fname = input().lower()  # One file name per line.
    if "." in fname:
        f_ext = fname.split('.')[-1]
        try:
            print(ext_dict[f_ext])
        except:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
        continue

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
