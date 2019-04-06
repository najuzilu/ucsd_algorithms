# python3

import sys
import threading

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

def stressTest():
    ''' read results '''
    with open('./tests/116.a') as f:
        output = f.read().splitlines()
    ''' reads input '''
    with open('./tests/116') as nf:
        read = nf.read().splitlines()

    global init_max, rank, parent, lines
    n, m = int(read[0].split()[0]), int(read[0].split()[1])
    lines = [int(x) for x in read[1].split()]
    rank = [1] * n
    parent = list(range(0, n))
    init_max = [max(lines)]

    for i in range(m):
        destination, source = int(read[i+2].split()[0]), int(read[i+2].split()[1])
        merge(destination - 1, source - 1)
        if (init_max[0]) != int(output[i]):
            print('not same: init_max={}  output={}'.format(init_max[0], output[i]))

def main():
    global init_max, rank, parent, lines
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))
    rank = [1] * n
    parent = list(range(0, n))
    init_max = [max(lines)]

    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        merge(destination - 1, source - 1)
        print(init_max[0])


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()