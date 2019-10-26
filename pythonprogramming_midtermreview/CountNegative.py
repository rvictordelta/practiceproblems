import sys
lns = sys.stdin.read().split("\n")

if lns[0] == 0:
    print(0)
else:
    print(len([x for x in lns[1].split() if int(x) < 0]))