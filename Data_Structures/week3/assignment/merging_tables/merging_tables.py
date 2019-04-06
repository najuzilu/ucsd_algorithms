# python3

import sys

def getParent(entry):
    if entry != parent[entry]:
        parent[entry] = getParent(parent[entry])
    return parent[entry]

def merge(destination, source):
    input1, input2 = getParent(destination), getParent(source)

    calc_value = 0

    if input1 == input2:
        return False

    if rank[input1] >= rank[input2]:
        parent[input2] = input1
        lines[input1] += lines[input2]
        lines[input2] = 0
        calc_value = lines[input1]
        if rank[input1] == rank[input2]:
            rank[input2] += 1
    else:
        parent[input1] = input2
        lines[input2] += lines[input1]
        lines[input1] = 0
        calc_value = lines[input2]

    if calc_value > init_max[0]:
        init_max[0] = calc_value
    return True

rank = [1] * n
parent = list(range(0, n))

init_max = [max(lines)]

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(init_max[0])