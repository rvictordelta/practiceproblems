test1 = """mentior
4
mentioromenas
asmentiorones
summentior
menolaxios"""

test2 = """ios
3
apalaxios
menolaxios
somolaxios"""

def counter(input):
    l = input.split('\n')
    com = l[0]
    names = l[2:]
    p = 0
    h = 0
    r = 0
    c = 0
    for n in names:
        if len(n) < len(com):
            c += 1
        elif n[:len(com)] == com:
            p += 1
        elif n[-len(com):] == com:
            h += 1
        elif com in n:
            r += 1
        else:
            c += 1

    out = f"""{p} PRINCESS
{h} BARON
{r} PRIEST
{c} COMMONER"""
    return out

print(counter(test1))
