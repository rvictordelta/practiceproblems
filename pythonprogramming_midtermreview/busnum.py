import sys
# test = """6
# 180 141 174 143 142 175"""

ln = sys.stdin.read().split('\n')[1].split()
# ln = test.split('\n')[1].split()
ln = [int(x) for x in ln]
ln = sorted(ln)

output = ''
run_counter = 0
for i, num in enumerate(ln):
    if run_counter > 1:
        run_counter -= 1
        continue
    j = i + 1
    active_run = True
    run_counter = 1
    while j < len(ln) and active_run:
        if ln[j-1] + 1 == ln[j]:
            run_counter += 1
            j += 1
        else:
            active_run = False
    if run_counter > 2:
        output += f'{ln[i]}-{ln[j-1]} '
        continue
    else:
        run_counter = 1
        output += f'{num} '

print(output)
