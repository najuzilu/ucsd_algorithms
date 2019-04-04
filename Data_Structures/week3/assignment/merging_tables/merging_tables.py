# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

rank = [0] * n
parent = list(range(0, n))

def getParent(entry):
    if entry != parent[entry]:
        parent[entry] = getParent(parent[entry])
    return parent[entry]

def merge(destination, source):
    input1, input2 = getParent(destination), getParent(source)

    if input1 == input2:
        return False

    if rank[input1] > rank[input2]:
        parent[input2] = input1
        lines[input1] += lines[source]
    else:
        parent[input1] = input2
        lines[input2] += lines[input1]
        if rank[input1] == rank[input2]:
            rank[input2] += 1
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(max(lines))