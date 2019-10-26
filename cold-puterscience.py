# test1 = """3
# 5 -10 15"""
#
# lns = test1.split("\n")
# lns = sys.stdin.read().split("\n")
# n = [1 for x in lns[1].split(" ") if int(x) < 0]
# print(sum(n))

import sys

# name = sys.stdin.read().split(" ")
name = "menolaxios mox"
name = name.split(" ")
l = len(name[1])
if l == 5:
    l = 4
print(name[0] +" " + name[1]*l)

