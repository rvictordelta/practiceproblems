test1 = """
1 1 1 1 2 1 3 1 1 2
"""

test2 = """
1 1 1 1 2 6 3 1 1 2
"""

test3 = """
5 5 4 5 3 5 2 5 4 3
"""

tests = [test1, test2, test3]


def cleantest(s):
    l = s.split(" ")
    l = [int(x) for x in l]
    if sum(l) >= 30 or max(l) > 5:
        print("CLEAN")
    else:
        print("DO NOT CLEAN")


for t in tests:
    cleantest(t)
