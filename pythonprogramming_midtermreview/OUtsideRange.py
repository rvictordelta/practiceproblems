import sys
x, y, z = sys.stdin.read().split()
if float(y) <= float(x) and float(x) <= float(z):
    print(False)
else:
    print(True)


