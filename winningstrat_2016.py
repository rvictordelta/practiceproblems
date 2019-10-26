t1= """100
5
4
0 1 0 0"""

t2= """140
20
8
0 0 0 1 0 1 1 1"""

t3 = """100
5
4
1 1 1 1"""

ts = [t1,t2,t3]

def martingaleyeah(s):
    l = s.split('\n')
    m = int(l[0]) # starting amount
    b = int(l[1]) # first bet

    flips = [int(x) for x in l[3].split(" ")]

    for flip in flips:
        if m < b:  # assuming this?  stricter than instructions say?
            return "BROKE"
        if flip == 1:
            m += b
            b = int(l[1])
            continue
        elif flip == 0:
            m -= b
            b = b*2
            continue
    return m

for t in ts:
    print(martingaleyeah(t))

